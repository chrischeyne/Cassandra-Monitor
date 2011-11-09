#!/usr/bin/env python
#
# -*- encoding: utf-8 -*-

#  
# 


# Wed Oct 12 16:33:11 BST 2011
""" Implements a simple Cassandra cluster mgt system
"""
__version_info__ = (0,1,4)
__author__ = "Chris Cheyne <chris@cheynes.org>"
__changelog__ = """
    Migrating away to use cluster=<map to C0,C0-DEV,C1-DEV> \
    0_1_3 shifting to manager->nodes
    0_1_4 moving to 'bubble' system to wrap conf
    """

try:
    # bring in environment variables
    from CLUSTER_ENVIRONMENT import *
    
    # ClusterShell ( pip install clustershell )
    from ClusterShell.NodeSet import NodeSet
    from ClusterShell.Task import task_self
    import os
    import string
    import datetime
    from socket import gethostname
except ImportError:
    raise ImportError('Please install clustershell >= 1.2.0')
    

    
# -----------------------------------------------------------------------------


def task_run(taskname,mynodes):
    """ run a specific command <taskname> on cluster <mynodes> """
    print "FULLRUN"
    task = task_self()
    print "Booting task: " , taskname
    
    # first initiate environment to run our python+java
    os.chdir(CASSANDRA_HOME)
    
    #FIXME: set init_environment to actually work
    #task.shell("cluster_config/init_environment.sh",nodes=mynodes)
    cmdenv = "export PYTHONHOME=/opt/python2.7.2; \
            export JAVA_HOME=/opt/jdk1.6.0_27; \
            export PYTHONPATH=/opt/python2.7.2/lib; \
            export \
            PATH=/opt/python2.7.2/lib:/opt/python2.7.2/bin:/opt/jdk1.6.0_27/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin;"
    

    
    task.run(cmdenv+taskname,nodes=mynodes)
    print ":\n".join(["%s=%s" % (i,j) for j,i in task.iter_buffers()])

def task_simplerun(taskname):
    """ task_simplerun(<argv2>)"""
    
    print "SIMPLERUN"
    task = task_self()
    print "Booting simpletask: " , taskname

    cmdenv = "export PYTHONHOME=/opt/python2.7.2; \
            export JAVA_HOME=/opt/jdk1.6.0_27; \
            export PYTHONPATH=/opt/python2.7.2/lib; \
            export \
            PATH=/opt/python2.7.2/lib:/opt/python2.7.2/bin:/opt/jdk1.6.0_27/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin;"
    
    task.run(cmdenv+taskname,nodes=RING_1_dev__allnodes)
    print ":\n".join(["%s=%s" % (i,j) for j,i in task.iter_buffers()])


def list_hosts():
    """ simply list hosts as we write """
    task_run("/bin/hostname -f",RING_1_dev__allnodes)

def cassandra_nodetool(mycluster=RING_1_dev__allnodes,cmd="ring"):
    """ display the status of the current cluster using nodetool """
    print CASSANDRA_NODETOOL
    cmd1 = CASSANDRA_NODETOOL + " -hlocalhost -p " + str(PORT) + " "
    task_run(cmd1+cmd,mycluster)
    
def cassandra_configured_tokens(mycluster=RING_1_dev__allnodes):
    """ display the status of the current cluster RING """
    task_run("cat "+ CASSANDRA_YAML + "|egrep \
            -i 'initial_token'",mycluster)


def cassandra_ring_status(mycluster=RING_1_dev__allnodes):
    """ display the status of the current cluster RING """
    cassandra_nodetool(mycluster)

def cassandra_histograms(mycluster=RING_1_dev__allnodes):
     """ display the status of the current cluster RING """
     cassandra_nodetool(mycluster,cmd="cfhistograms")



def cassandra_init(mycluster=RING_1_dev__allnodes):
    print "** BOOTING CASSANDRA CLUSTER **"
    os.chdir(CASSANDRA_HOME)
    task_run(CASSANDRA_INIT_SCRIPT + " start", mycluster)



def cassandra_stop(mycluster=RING_1_dev__allnodes):
    print "** Shutting down cassandra ... **"
    os.chdir(CASSANDRA_HOME)
    task_run(CASSANDRA_INIT_SCRIPT + " stop", mycluster) 


def cassandra_info(mycluster=RING_1_dev__allnodes):
    print "Cassandra INFO information..."
    os.chdir(CASSANDRA_HOME)

    cmd = "cfstats | egrep -i latency"
    cassandra_nodetool(mycluster,cmd)

def cassandra_get_keyspaces():
    print "Cassandra RING information..."
    os.chdir(CASSANDRA_HOME)
    task.run(CASSANDRA_BIN + "/bin/nodetool -hlocalhost -p" + str(PORT) + " ring",nodes=RING_1_dev__bootstrapnodes)



def cassandra_stress_test(cluster=RING_1_dev__allnodes):
    print "Stress testing CLUSTER %s",cluster
    os.chdir(CASSANDRA_CORE)
    task_run(CASSANDRA_CORE + "/cluster-node-stress-test.sh",cluster)



def cassandra_load_schema(self,cluster="RING_1_dev_allnodes",filename="schema.txt"):
    
    print "Instigating schema on cluster "+cluster
    os.chdir(CASSANDRA_HOME)
    task_run(CASSANDRA_BIN + "/cassandra-cli -hlocalhost -p" +str(PORT) + "-f \
            "+filename, nodes=RING_1_dev__bootstrapnodes)

def cassandra_listening(mycluster=RING_1_dev__allnodes):

    print "**LISTENING** ON CLUSTER ..." ,mycluster
    os.chdir(CASSANDRA_HOME)
    task_run("netstat -an |egrep -i '(9160|7199|9159|7198)' | awk \
            '{print $4}'", mycluster)
    print "**\tRPC PORTS CONFIGURED..."

    task_run("cat "+ CASSANDRA_YAML + "|egrep \
            -i '(rpc_port|rpc_address)'",mycluster)



def jdk_getversion(mycluster=RING_1_dev__allnodes):
    print "** JDK VERSIONS **"
    print "Java home is " , os.environ["JAVA_HOME"]
    os.chdir(JAVA_HOME)
    task_run(JAVA_HOME + "/bin/javac -version", mycluster)

def py_getversion(mycluster=RING_1_dev__allnodes):
    print "** PYTHON VERSIONS **"
    print "PYTHON home is " , os.environ["PYTHONHOME"]
    os.chdir(PYTHONHOME)
    task_run(PYTHONHOME + "/bin/python -V", mycluster)


 
def myport_scan(mycluster=RING_1_dev__allnodes,myport=7199):
    print "Port scanning for node listening..." , mycluster, myport
    
    task_run("fuser -v " + str(myport) + "/tcp",mycluster)




def init_environment(mycluster=RING_1_dev__allnodes):
        
    os.environ["PYTHONHOME"]=PYTHONHOME
    os.environ["PYTHONPATH"]=PYTHONPATH
    os.environ["JAVA_HOME"]=JAVA_HOME
    sys.prefix=PYTHONHOME
    sys.exec_prefix=PYTHONHOME
    sys.path.append(PYTHONHOME)
    sys.path.append(PYTHONPATH)
    os.chdir(PYTHONHOME)
    print "init_environment(): path is ",PATH," pythonhome is, ", PYTHONHOME

# initialise rings from config file
print "python home is now " , PYTHONHOME , "ring 1 is " , RING_1_dev__allnodes

# -- MAIN --


if __name__ == "__main__":
    
    
    import sys,os
   
       
    #FIXME: obvious.
    cmd = int(sys.argv[1])
    os.chdir(CASSANDRA_HOME)
    os.system('clear')
    #init_environment()
    list_hosts()
    
    # FIXME: luban/django interface 
    # pass in 1 to boot cluster    
    if cmd == 1:
        cassandra_init()
    # 2 to shutdown-
    if cmd == 2:
        cassandra_stop()
    if cmd == 3:
        cassandra_load_schema(self,sys.argv[2])
    if cmd == 4:
        cassandra_listening()
    if cmd == 5:
        cassandra_info()
    if cmd == 6:
        cassandra_configured_tokens()
    if cmd == 7:
        cassandra_stress_test()
    if cmd == 8:
        cassandra_ring_status()
    if cmd == 9:
        cassandra_histograms()


    # run argument 2 quickly from cli ..mgr.py 10 "hostname -f" 
    if cmd == 10:
            print "arguments"
            print sys.argv
            task_simplerun(sys.argv[2])
    if cmd == 11:
        myport_scan()
    if cmd == 12:
        jdk_getversion()
    if cmd == 13:
        py_getversion()




