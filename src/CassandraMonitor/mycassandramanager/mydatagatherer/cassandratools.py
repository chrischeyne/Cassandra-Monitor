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


# Mon Dec  5 14:48:38 GMT 2011
# UNDER UNIT TESTING


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
from ClusterShell.Task import taskself
from socket import gethostname

# -----------------------------------------------------------------------------


def taskrun(taskname,mynodes):
    """ run a specific command <taskname> on cluster <mynodes> """
    task = taskself()
    
    # first initiate environment to run our python+java
    os.chdir(CASSANDRAHOME)
    task.run(cmdenv+taskname,nodes=mynodes)
    print ":\n".join(["%s=%s" % (i,j) for j,i in task.iterbuffers()])

def tasksimplerun(taskname):
    """ tasksimplerun(<argv2>)"""
    
    task = taskself()
    task.run(cmdenv+taskname,nodes=RING1devallnodes)
    print ":\n".join(["%s=%s" % (i,j) for j,i in task.iterbuffers()])


def listhosts(ring):
    """ simply list hosts as we write """
    taskrun("/bin/hostname -f",ring)

def cassandranodetool(mycluster=RING1devallnodes,cmd="ring"):
    """ display the status of the current cluster using nodetool """
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

# -- MAIN --

if name == "main":
       
    #FIXME: obvious.  Apply error-checking and chained arguments
    cmd = int(sys.argv[1])
    ring = str(sys.argv[2])

    initenvironment()
    listhosts()
    
    if cmd == 1:
        cassandrainit()
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
            tasksimplerun(sys.argv[2])
    if cmd == 11:
        myportscan()
    if cmd == 12:
        jdkgetversion()
    if cmd == 13:
        pygetversion()




