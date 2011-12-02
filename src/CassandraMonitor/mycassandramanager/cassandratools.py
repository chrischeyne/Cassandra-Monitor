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

"""
cassandratools - cassandra management tools. Wrapper around nodetool
ClusterSSH

"""
author = "Chris T. Cheyne"
copyright = "Copyright 2011, The Cassandra Manager Project"
credits = ["Chris Cheyne"]
license = "GPL"
version = "0.0.1"
maintainer = "Chris T. Cheyne"
email = "maintainer@cassandra-manager.org"
status = "Alpha"


try:
    # bring in environment variables
    import mylogger.logger as loggingsystem
    SYSLOG = loggingsystem.MyLogger()
    SYSLOG.l.debug('booting....')
    import myconfig.config as config
    SYSCONFIG = config.MyConfig()
    SYSLOG.l.info('mysql host is %s ' % SYSCONFIG.conf['mysql']['host'])

    # ClusterShell ( pip install clustershell )
    from ClusterShell.NodeSet import NodeSet
    from ClusterShell.Task import taskself
    import os
    import string
    import datetime
    from socket import gethostname
except ImportError:
    raise ImportError('Please install clustershell >= 1.2.0')
# -----------------------------------------------------------------------------


def taskrun(taskname,mynodes):
    """ run a specific command <taskname> on cluster <mynodes> """
    print "FULLRUN"
    task = taskself()
    print "Booting task: " , taskname
    
    # first initiate environment to run our python+java
    os.chdir(CASSANDRAHOME)
    
    #FIXME: set initenvironment to actually work
    #task.shell("clusterconfig/initenvironment.sh",nodes=mynodes)
    cmdenv = "export PYTHONHOME=/opt/python2.7.2; \
            export JAVAHOME=/opt/jdk1.6.027; \
            export PYTHONPATH=/opt/python2.7.2/lib; \
            export \
            PATH=/opt/python2.7.2/lib:/opt/python2.7.2/bin:/opt/jdk1.6.027/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin;"
    

    
    task.run(cmdenv+taskname,nodes=mynodes)
    print ":\n".join(["%s=%s" % (i,j) for j,i in task.iterbuffers()])

def tasksimplerun(taskname):
    """ tasksimplerun(<argv2>)"""
    
    print "SIMPLERUN"
    task = taskself()
    print "Booting simpletask: " , taskname

    cmdenv = "export PYTHONHOME=/opt/python2.7.2; \
            export JAVAHOME=/opt/jdk1.6.027; \
            export PYTHONPATH=/opt/python2.7.2/lib; \
            export \
            PATH=/opt/python2.7.2/lib:/opt/python2.7.2/bin:/opt/jdk1.6.027/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin;"
    
    task.run(cmdenv+taskname,nodes=RING1devallnodes)
    print ":\n".join(["%s=%s" % (i,j) for j,i in task.iterbuffers()])


def listhosts():
    """ simply list hosts as we write """
    taskrun("/bin/hostname -f",RING1devallnodes)

def cassandranodetool(mycluster=RING1devallnodes,cmd="ring"):
    """ display the status of the current cluster using nodetool """
    print CASSANDRANODETOOL
    cmd1 = CASSANDRANODETOOL + " -hlocalhost -p " + str(PORT) + " "
    taskrun(cmd1+cmd,mycluster)
    
def cassandraconfiguredtokens(mycluster=RING1devallnodes):
    """ display the status of the current cluster RING """
    taskrun("cat "+ CASSANDRAYAML + "|egrep \
            -i 'initialtoken'",mycluster)


def cassandraringstatus(mycluster=RING1devallnodes):
    """ display the status of the current cluster RING """
    cassandranodetool(mycluster)

def cassandrahistograms(mycluster=RING1devallnodes):
     """ display the status of the current cluster RING """
     cassandranodetool(mycluster,cmd="cfhistograms")



def cassandrainit(mycluster=RING1devallnodes):
    print "** BOOTING CASSANDRA CLUSTER **"
    os.chdir(CASSANDRAHOME)
    taskrun(CASSANDRAINITSCRIPT + " start", mycluster)


def cassandrastop(mycluster=RING1devallnodes):
    print "** Shutting down cassandra ... **"
    os.chdir(CASSANDRAHOME)
    taskrun(CASSANDRAINITSCRIPT + " stop", mycluster) 


def cassandrainfo(mycluster=RING1devallnodes):
    print "Cassandra INFO information..."
    os.chdir(CASSANDRAHOME)

    cmd = "cfstats | egrep -i latency"
    cassandranodetool(mycluster,cmd)

def cassandragetkeyspaces():
    print "Cassandra RING information..."
    os.chdir(CASSANDRAHOME)
    task.run(CASSANDRABIN + "/bin/nodetool -hlocalhost -p" + str(PORT) + " ring",nodes=RING1devbootstrapnodes)



def cassandrastresstest(cluster=RING1devallnodes):
    print "Stress testing CLUSTER %s",cluster
    os.chdir(CASSANDRACORE)
    taskrun(CASSANDRACORE + "/cluster-node-stress-test.sh",cluster)



def cassandraloadschema(self,cluster="RING1devallnodes",filename="schema.txt"):
    
    print "Instigating schema on cluster "+cluster
    os.chdir(CASSANDRAHOME)
    taskrun(CASSANDRABIN + "/cassandra-cli -hlocalhost -p" +str(PORT) + "-f \
            "+filename, nodes=RING1devbootstrapnodes)

def cassandralistening(mycluster=RING1devallnodes):

    print "**LISTENING** ON CLUSTER ..." ,mycluster
    os.chdir(CASSANDRAHOME)
    taskrun("netstat -an |egrep -i '(9160|7199|9159|7198)' | awk \
            '{print $4}'", mycluster)
    print "**\tRPC PORTS CONFIGURED..."

    taskrun("cat "+ CASSANDRAYAML + "|egrep \
            -i '(rpcport|rpcaddress)'",mycluster)



def jdkgetversion(mycluster=RING1devallnodes):
    print "** JDK VERSIONS **"
    print "Java home is " , os.environ["JAVAHOME"]
    os.chdir(JAVAHOME)
    taskrun(JAVAHOME + "/bin/javac -version", mycluster)

def pygetversion(mycluster=RING1devallnodes):
    print "** PYTHON VERSIONS **"
    print "PYTHON home is " , os.environ["PYTHONHOME"]
    os.chdir(PYTHONHOME)
    taskrun(PYTHONHOME + "/bin/python -V", mycluster)


 
def myportscan(mycluster=RING1devallnodes,myport=7199):
    print "Port scanning for node listening..." , mycluster, myport
    
    taskrun("fuser -v " + str(myport) + "/tcp",mycluster)




def initenvironment(mycluster=RING1devallnodes):
        
    os.environ["PYTHONHOME"]=PYTHONHOME
    os.environ["PYTHONPATH"]=PYTHONPATH
    os.environ["JAVAHOME"]=JAVAHOME
    sys.prefix=PYTHONHOME
    sys.execprefix=PYTHONHOME
    sys.path.append(PYTHONHOME)
    sys.path.append(PYTHONPATH)
    os.chdir(PYTHONHOME)
    print "initenvironment(): path is ",PATH," pythonhome is, ", PYTHONHOME

# initialise rings from config file
print "python home is now " , PYTHONHOME , "ring 1 is " , RING1devallnodes

# -- MAIN --


if name == "main":
    
    
    import sys,os
   
       
    #FIXME: obvious.
    cmd = int(sys.argv[1])
    os.chdir(CASSANDRAHOME)
    os.system('clear')
    #initenvironment()
    listhosts()
    
    # FIXME: luban/django interface 
    # pass in 1 to boot cluster    
    if cmd == 1:
        cassandrainit()
    # 2 to shutdown-
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


    # run argument 2 quickly from cli ..mgr.py 10 "hostname -f" 
    if cmd == 10:
            print "arguments"
            print sys.argv
            tasksimplerun(sys.argv[2])
    if cmd == 11:
        myportscan()
    if cmd == 12:
        jdkgetversion()
    if cmd == 13:
        pygetversion()




