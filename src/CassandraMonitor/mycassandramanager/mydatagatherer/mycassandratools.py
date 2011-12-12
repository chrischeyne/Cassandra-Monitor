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


# Mon Dec 12 11:35:09 GMT 2011
# =====
# UNDER UNIT TESTING - LOCAL COPIES OF MYCONFIG{py,yaml} MYLOGGER
# RETURN MODIFIED COPIES TO myconfig/
# =====

"""
cassandratools - cassandra management tools. Wrapper around nodetool using 
ClusterSSH and bubble configlets

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
print sys.path
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

# -----------------------------------------------------------------------------
class MyNodeTool():
    """ run command <cmd> on host <host> """
    """ defaults to a single node """
    myhost = None
    mycmd = None
    myring = None


    def __init__(self,ring='ringlive',host='florence',cmd='info'):
        self.myhost = host
        self.mycmd = cmd
        self.myring = ring
        NT = "nodetool" 
        pass

    def nodetool(self,cmd='info'):
        """ run nodetool command <c>"""
        """ on ring <ring>"""
        """ nodetool object should be dynamic as config is dynamic """
        print "NOTETOOL() booting on ring,host,cmd " ,self.myring, self.myhost,cmd
        NT = SYSCONFIG.conf[self.myring]['CASSANDRAHOME'] \
                + SYSCONFIG.conf[self.myring]['nodetool']
        NT = str(NT) + " -h " + str(self.myhost)
        NT = str(NT) + " -p " + str(SYSCONFIG.conf[self.myring]['cassrpc'])
        print "cmd NT is ",cmd, " " , NT
        return NT

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

class CassandraTools():
    """ our CassandraTools collection of objects to operate on a casssandra
    cluster """
    # default nodes, empty if not initialised
    mynodes = None
    myring = None
    mybubbles = \
    dict(zip(('bootcassie','stopcassie','migratecassie','mutatecassie'),
        (1,2,3,4)))

    def __init__(self,ring):
        """ initialise, set our current operational ring """
        """ set our list of nodes """

        self.myring = ring
        self.mynodes = self.getnodes(self.myring) 
        pass

    def cmdenv(self):
        """ configure the environment for clusterssh """
        """ to ensure we run correct python/java etc """
        from os import environ as env
        environment = env['HOME']
        return environment

    def configuredtokens(self):
        """ display the status of the current cluster token information """
        nt = MyNodeTool(self.myring,'localhost','info')
        cmd = nt.nodetool()
        print "configuredtokens(): cmd is ",cmd
        tokens = dict(self.taskrunlocal(cmd))
        print "configuredtokens:  ",tokens
        pass


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

    def taskrunring(self,taskname,myring):
        """ run a specific command <taskname> on ring <mynodes> """
        task = task_self()
        myenv = self.cmdenv()
        mynodes = mycassietools.getnodes(myring)
        # first initiate environment to run our python+java
        SYSCONFIG.conf[myring]['CASSANDRAHOME']
        os.chdir(SYSCONFIG.conf[myring]['CASSANDRAHOME'])
        # FIXME: initenvironment?
        task.run(taskname,nodes=mynodes)
        # FIXME: return data in dictionarys for mydatatools
        print ":\n".join(["%s=%s" % (i,j) for j,i in task.iter_buffers()])

    def taskrunlocal(self,cmd):
        """ taskrunlocal - run <taskname> on localhost """
        """ note I have kept this isolated from taskrunring for plugin use """
        task = task_self()
        myenv = self.cmdenv()
        print "runlocal: env is ",myenv
        print "runlocal: cmd is ",cmd
        task.run(myenv+cmd,nodes='localhost')
        # FIXME: return data in dicts
        mydict = dict({'one':1,'two':2})
        print ":\n".join(["%s=%s" % (i,j) for j,i in task.iter_buffers()])
        return mydict

    def listhosts(self,myring):
        """ retrieve kernel versions """ 
        self.taskrunring("/bin/uname -r",myring)

    # FIXME: DAEMONIZE see http://pypi.python.org/pypi/python-daemon/

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

    def cassandrainfo(self,mycluster=mynodes):
        print "Cassandra INFO information..."
        os.chdir(CASSANDRAHOME)

        cmd = "cfstats | egrep -i latency"
        cassandranodetool(mycluster,cmd)
        os.chdir(CASSANDRAHOME)
        task.run(CASSANDRABIN + "/bin/nodetool -hlocalhost -p" + str(PORT) + " ring",nodes=RING1devbootstrapnodes)



    def cassandrastresstest(self,cluster=mynodes):
        print "Stress testing CLUSTER %s",cluster
        os.chdir(CASSANDRACORE)
        taskrunring(CASSANDRACORE + "/cluster-node-stress-test.sh",cluster)



    def cassandraloadschema(self,cluster="mynodes",filename="schema.txt"):
        
        print "Instigating schema on cluster "+cluster
        os.chdir(CASSANDRAHOME)
        taskrunring(CASSANDRABIN + "/cassandra-cli -hlocalhost -p" +str(PORT) + "-f \
                "+filename, nodes=RING1devbootstrapnodes)

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

    def initenvironment(self,mycluster=mynodes):
        """ ensure clusterSSH is running in the correct environment"""
        """ this ensures system python etc does not get in the way"""
        """ read in environment variables from myconfig """
        os.environ["PYTHONHOME"]=PYTHONHOME
        os.environ["PYTHONPATH"]=PYTHONPATH
        os.environ["JAVAHOME"]=JAVAHOME
        sys.prefix=PYTHONHOME
        sys.execprefix=PYTHONHOME
        sys.path.append(PYTHONHOME)
        sys.path.append(PYTHONPATH)
        os.chdir(PYTHONHOME)
        print "initenvironment(): path is ",PATH," pythonhome is, ", PYTHONHOME

# -----------------------------------------------------------------------------

# -- MAIN --
if __name__ == "__main__":

    #FIXME: obvious.  Apply error-checking and chained arguments
    cmd = int(sys.argv[1])
    ring = str(sys.argv[2])
    print "Running ",cmd," on ring ",ring, " ...", "with nodes: -"
    mycassietools = CassandraTools('ringlive')
    mynodes = mycassietools.getnodes('ringlive')
    for j in mynodes:
        print j
    mycassietools.listhosts('ringlive')
    #sys.exit(1)


    
    if cmd == 1:
        mycassietools.configuredtokens()
        mycassietools.ringstatus()
        mycassietools.histograms()
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




