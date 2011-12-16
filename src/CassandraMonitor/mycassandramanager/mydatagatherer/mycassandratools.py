#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


#Fri Dec 16 09:31:53 GMT 2011
# =====
# UNDER UNIT TESTING - LOCAL COPIES OF MYCONFIG{py,yaml} MYLOGGER
# RETURN MODIFIED COPIES TO myconfig/
# =====

"""
cassandratools - cassandra management tools. Wrapper around nodetool using 
ClusterSSH and bubble configlets.  Each bubble insolates the working
environment and passes that to ClusterSSH.  In other words: -

stdout,stderr = EXECUTE(command <-- get(bubbleenv,bubblecmd))


"""
author = "Chris T. Cheyne"
copyright = "Copyright 2011, The Cassandra Manager Project"
credits = ["Chris Cheyne"]
license = "GPL"
version = "0.0.1"
maintainer = "Chris T. Cheyne"
email = "maintainer@cassandra-manager.org"
status = "Alpha"

# FIXME: contained in datagatherer.py
from operator import itemgetter, attrgetter
import os
import sys
import string
import datetime

# FIXME: remove after unit testing
APPEND=os.path.dirname(__file__)
sys.path.append(APPEND)
sys.path.append('\
/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager')
sys.path.append('\
/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/mydatagatherer')
sys.path.append('\
/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/mydatagatherer/myconfig')
sys.path.append('\
/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/mydatagatherer/mylogger')
# bring in environment variables
import mylogger.logger as loggingsystem
SYSLOG = loggingsystem.MyLogger()
SYSLOG.l.debug('booting....')
import myconfig.config as config
SYSCONFIG = config.MyConfig()
SYSLOG.l.info('mysql host is %s ' % SYSCONFIG.conf['mysql']['host'])
# ClusterShell ( pip install clustershell )
from ClusterShell.NodeSet import NodeSet
from ClusterShell.Task import task_self
from socket import gethostname
import time

# -----------------------------------------------------------------------------
class MyNodeTool():
    """ run command <cmd> on host <host> """
    """ defaults to a single node and the info command """
    myhost = None
    mycmd = None
    myring = None

    def __init__(self,ring='ringlive',host='florence',cmd='info'):
        self.myhost = host
        self.mycmd = cmd
        self.myring = ring
        NT = "nodetool" 

    def nodetool(self,cmd='info'):
        """ run nodetool command <c>"""
        """ on ring <ring>"""
        """ nodetool object should be dynamic as config is dynamic  """
        """ thus e.g. the port might change each time we are called """
        NT = SYSCONFIG.conf[self.myring]['CASSANDRAHOME'] \
                + SYSCONFIG.conf[self.myring]['nodetool']
        NT = str(NT) + " -h " + str(self.myhost)
        NT = str(NT) + " -p " + str(SYSCONFIG.conf[self.myring]['cassrpc'])
        NT = NT + " ",cmd
        #returns a tuple of (nodetool,cmd)
        return NT

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

class Timeout(Exception):
    """ fixme: report properly """
    """ used for run() as an exception handler """
    pass

class CassandraTools():
    """ our CassandraTools collection of objects to operate on a casssandra
    cluster """
    # default nodes, empty if not initialised
    # FIXME: bring in dictionary tools module
    mynodes = None
    myring = None
    mybubbleinitcmds = None
    mybubblecmds = None
    

    def __init__(self,ring):
        """ initialise, set our current operational ring """
        """ set our list of nodes """
        """ set our Cassandra commands """
        self.myring = ring
        self.mynodes = self.getnodes(self.myring) 

        #FIXME: get from myconfig -> 1,2,3,4
        pairs = \
        dict(zip(('bootcassie','stopcassie','migratecassie','mutatecassie'\
        ),
        (None,None,None,None)))
        self.mybubbleinitcmds = zip(pairs.iterkeys(),pairs.itervalues())

        infocmds = \
        ['ring','join','info','cfstats','clearsnapshot',\
        'version','tpstats','drain','decommission','loadbalance',\
        'compactionstats','disablegossip','enablegossip',\
        'disablethrift','enablethrift','snapshot','netstats',\
        'move','removetoken','flush','repair','cleanup',\
        'compact','scrub','invalidatekeycache',\
        'invalidaterowcache','getcompactionthreshold',\
        'cfhistograms','setcachecapacity','setcompactionthreshold']

        self.mybubblecmds = dict.fromkeys(infocmds,None)
        pass

    
    
    def _getbubble(self,system):
        """" return dict of the current environment for current ring """
        x = sorted(SYSCONFIG.conf[self.myring].items(), key=itemgetter(1))
        return dict(x)
    
    def _generateenv(self,cmd,isNormal=True):
        """ basically generates a file containing cmd to give to run() """
        """ that contains a file for shell to source and then """
        """ run cassandra inside """
        """ if isNormal: 'run normal command' else 'init command'"""

        myfile = './cassandra.sh'
        env = os.environ
        cassenv = self._getbubble('cassandra')
        # replace current environment variables with our bubble
        mykeys = ('PYTHONHOME',
                'PYTHONPATH',
                'CASSANDRAHOME',
                'JAVA_HOME')
        try:
            for k in mykeys:
                env[k] = env.get(k,cassenv[k])
        except KeyError:
            env[k] = cassenv[k]
        # generate our executable script, complete with environment
        # FIXME: this is not portable!
        # FIXME: bring in generator tools! 
        root = SYSCONFIG.conf[self.myring]['CASSANDRAHOME']
        with open(root+'/cassandrarun.sh','w') as f:
            f.write("#!/usr/bin/env bash")
            f.write('\n')
            for key in cassenv.keys():
                mystr = 'export '+str(key)+'='+str(cassenv[key])
                f.write(mystr)
                f.write('\n')

            f.write('\n')

        print 'wrote file %s' % myfile

        # return the filename and the environment for run()
        return myfile,cassenv
    
    def _generatecmd(self,cmd,myfile,isNormal=True):
        """ appends the cmd bubble to the env bubble """
        """ sets final bubble +x """
        """ this is run by ClusterShell """
        print '_cmd file is',myfile,isNormal
        root = SYSCONFIG.conf[self.myring]['CASSANDRAHOME']
        with open(root+'/cassandrarun.sh','a') as f:
            f.write('# COMMAND LAUNCHER\n')
            f.write(cmd)
            f.write('\n')


        print 'write file %s' %myfile



    def run(self,cmd,timeout=10):
        """ run a local command avoiding ClusterSSH; capture output """
        """ returns stdout,stderr,returncode """
        """ FIXME: put in module """
        import subprocess as sub
        # first we set up the environment for the current cassie
        # by getting current environment and remapping with
        # _generate{env,cmd=(init||normal)}
        isinitcmd = True
        isinitcmd = self.mybubblecmds.has_key(cmd) 

        myfile,cassenv = self._generateenv(cmd,isinitcmd)
        self._generatecmd(cmd,myfile,isinitcmd)

        sys.prefix = cassenv['PYTHONHOME']
        sys.execprefix = cassenv['PYTHONHOME']
        sys.path.append(cassenv['PYTHONHOME'])
        sys.path.append(cassenv['JAVA_HOME'])
        sys.path.append(cassenv['PYTHONPATH'])
        os.chdir(cassenv['PYTHONHOME'])
        # then we boot the run command, running in the environment and return
        # STD{out,err} <-- FIXME: stderr catch
        print 'RUN():  booting command ',cmd
        sub.Popen(cmd,stdout=sub.PIPE,shell=True).stdout.read()
        print '------------------------------'
        pass


    def configuredtokens(self):
        """ display the status of the current cluster token information """
        nt = MyNodeTool(self.myring,'localhost','info')
        cmd = nt.nodetool()
        tokens = dict(self.taskrunlocal(cmd))
        print "configuredtokens:  ",tokens

    def ringstatus(self):
        """ display the status of the current cluster RING """
        ringstatus = {}
        nt = MyNodeTool(self.myring,'localhost','info')
        cmd = nt.nodetool()
        ringstatus = dict(self.taskrunlocal(cmd))
        return ringstatus

    def histograms(self):
        """ display the status of the current cluster RING """
        histograms = {}
        nt = MyNodeTool(self.myring,'localhost','info')
        cmd = nt.nodetool()
        histograms = dict(self.taskrunlocal(cmd))
        return histograms


    def getnodes(self,ring):
        """ return nodes from ring ring """
        """ FIXME: return to mydatatools.py """
        x = sorted(SYSCONFIG.conf[ring]['nodes'].values(),key = itemgetter(1))
        mynodeset = NodeSet.fromlist(x)
        return mynodeset

    def taskrunring(self,taskname):
        """ run a specific command <taskname> on ring <mynodes> """
        myring = self.myring
        task = task_self()
        mynodes = mycassietools.getnodes(myring)
        SYSCONFIG.conf[myring]['CASSANDRAHOME']
        task.run(taskname,nodes=mynodes)
        print "VECTOR RUN RING"
        print ":\n".join(["%s=%s" % (i,j) for j,i in task.iter_buffers()])
        mydict = dict({'one':1,'two':2})
        return mydict

    def taskrunlocal(self,cmd):
        """ taskrunlocal - run <taskname> on localhost """
        """ note I have kept this isolated from taskrunring for plugin use """
        myring = self.myring
        task = task_self()
        localcmd = cmd[0]+cmd[1]
        stdout = self.run(localcmd)
        mydict = dict({'one':1,'two':2})
        print "VECTOR RUN LOCAL"
        print stdout
        return mydict

    def listhosts(self,myring):
        """ retrieve kernel versions """ 
        self.taskrunring("/bin/uname -r")

    # FIXME: DAEMONIZE see http://pypi.python.org/pypi/python-daemon/
    # daemon commands, such as start cluster, migrate, mutate
    # -------------------------------------------------------------------------
    def cassandrainit(self,mycluster=mynodes):
        print "** BOOTING CASSANDRA CLUSTER **"
        os.chdir(CASSANDRAHOME)
        taskrunring(CASSANDRAINITSCRIPT + " start", mycluster)


    def cassandrastop(self,mycluster=mynodes):
        print "** Shutting down cassandra ... **"
        os.chdir(CASSANDRAHOME)
        taskrunring(CASSANDRAINITSCRIPT + " stop", mycluster) 

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # normal commands, such as ring info
    # -------------------------------------------------------------------------
    def cassandrainfo(self,mycluster=mynodes):
        print "Cassandra INFO information..."
        os.chdir(CASSANDRAHOME)
        cmd = "cfstats | egrep -i latency"
        os.chdir(CASSANDRAHOME)
        pass

    def cassandrastresstest(self,cluster=mynodes):
        print "Stress testing CLUSTER %s",cluster
        os.chdir(CASSANDRACORE)
        pass

    def cassandraloadschema(self,cluster="mynodes",filename="schema.txt"):
        print "Instigating schema on cluster "+cluster
        os.chdir(CASSANDRAHOME)
        pass

    def cassandralistening(self,mycluster=mynodes):
        print "**LISTENING** ON CLUSTER ..." ,mycluster
        os.chdir(CASSANDRAHOME)
        taskrunring("netstat -an |egrep -i '(9160|7199|9159|7198)' | awk \
                '{print $4}'", mycluster)
        print "**\tRPC PORTS CONFIGURED..."

        taskrunring("cat "+ CASSANDRAYAML + "|egrep \
                -i '(rpcport|rpcaddress)'",mycluster)



    def jdkgetversion(self,mycluster=mynodes):
        print "** JDK VERSIONS **"
        print "Java home is " , os.environ["JAVAHOME"]
        os.chdir(JAVAHOME)
        taskrunring(JAVAHOME + "/bin/javac -version", mycluster)

    def pygetversion(self,mycluster=mynodes):
        print "** PYTHON VERSIONS **"
        print "PYTHON home is " , os.environ["PYTHONHOME"]
        os.chdir(PYTHONHOME)
        taskrunring(PYTHONHOME + "/bin/python -V", mycluster)


    def myportscan(self,mycluster=mynodes,myport=7199):
        print "Port scanning for node listening..." , mycluster, myport
        taskrunring("fuser -v " + str(myport) + "/tcp",mycluster)

# -----------------------------------------------------------------------------

# -- MAIN --
if __name__ == "__main__":

    #FIXME: obvious.  Apply error-checking and chained arguments
    cmd = int(sys.argv[1])
    ring = str(sys.argv[2])
    print "Running ",cmd," on ring ",ring, " ...", "with nodes: -"
    mycassietools = CassandraTools(ring)
    mynodes = mycassietools.getnodes(ring)
    for j in mynodes:
        print j
    mycassietools.listhosts(ring)
    
    if cmd == 1:
        # FIXME: initial testing
        mycassietools.configuredtokens()
        #mycassietools.ringstatus()
        #mycassietools.histograms()
        #cassandrainit()
    if cmd == 2:
        cassandrastop()
    if cmd == 3:
        cassandraloadschema(self,sys.argv[2])
    if cmd == 4:
        cassandralistening()
    if cmd == 5:
        cassandrainfo()
    if cmd == 6:
        cassandraconfiguredtokens()
    if cmd == 7:
        cassandrastresstest()
    if cmd == 8:
        cassandraringstatus()
    if cmd == 9:
        cassandrahistograms()


    # simply run argument 2 quickly from cli cassandratools.py 10 "hostname -f" 
    if cmd == 10:
            print "arguments"
            print sys.argv
            taskrunlocal(sys.argv[2])
    if cmd == 11:
        myportscan()
    if cmd == 12:
        jdkgetversion()
    if cmd == 13:
        pygetversion()




