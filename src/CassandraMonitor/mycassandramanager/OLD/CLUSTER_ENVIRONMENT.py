#!/opt/python-2.7.2/bin/python
# 

# Thu Oct 27 18:22:37 BST 2011
# 
try:
   # ClusterShell ( pip install clustershell )
    from ClusterShell.NodeSet import NodeSet
    from ClusterShell.Task import task_self
except ImportError:
    raise ImportError('Please install clustershell >= 1.2.0')
 
# RING0
RING0DEV=["10.10.1.39","10.10.1.40","10.10.1.43","10.10.1.50"]
RING0LIVE=[]

RING1DEV=["10.10.1.39","10.10.1.40","10.10.1.43","10.10.1.50"]
RING1LIVE=[]

# initialise rings from config file
RING_1_dev__allnodes  = NodeSet.fromlist(RING1DEV)
RING_1_dev__bootstrapnode = NodeSet.fromlist(RING1DEV)


# CASSANDRA
CASSANDRA_VERSION="0.8.5"
CASSANDRA_CORE="/opt/cassandra-dev"
CASSANDRA_HOME=CASSANDRA_CORE +"/apache-cassandra-" + CASSANDRA_VERSION
CASSANDRA_BIN=CASSANDRA_HOME +"/bin/cassandra"
CASSANDRA_CONF=CASSANDRA_CORE +"/cluster_config"
CASSANDRA_INCLUDE=CASSANDRA_CONF +"/cassandra.in.sh"
# JMX port
PORT=7198
CASSANDRA_STRESS_TEST=CASSANDRA_HOME+"/SOFTWARE/apache-cassandra-0.8.6-src/tools/stress/bin/stress"

# CASSANDRA.YAML
CASSANDRA_YAML=CASSANDRA_CORE+ "/cluster_config/cassandra.yaml"
CASSANDRA_INIT_SCRIPT=CASSANDRA_CONF + "/cassandra-dev-init.sh"
CASSANDRA_YAML_FILE="-Dcassandra.config=file:" +CASSANDRA_YAML
CASSANDRA_NODETOOL=CASSANDRA_HOME +"/bin/nodetool"
# LOCK FILES - IMPORTANT FOR SHUTDOWN
CASSANDRA_LOG=CASSANDRA_CORE +"/log/cassandra.log"
CASSANDRA_PID=CASSANDRA_CORE +"/run/cassandra.pid"
CASSANDRA_LOCK=CASSANDRA_CORE +"+/lock/subsys/cassandra"
PROGRAM="cassandra"

# JDK AND ANT
JAVA_VERSION="1.6.0_27"
ANT_VERSION="1.8.2"
JAVA_HOME="/opt/jdk" + JAVA_VERSION
CLASSPATH=JAVA_HOME + ":" + CASSANDRA_HOME + "/lib"
ANT_HOME="/opt/" + JAVA_HOME + "/apache-ant-" + ANT_VERSION



# PYTHON
PYTHON_VERSION="2.7.2"
PYTHONHOME="/opt/python-" + PYTHON_VERSION
PYTHONPATH=PYTHONHOME + "/lib"
PYHOME=PYTHONHOME

# MAVEN
M2_VERSION="3.0.3"
M2_HOME= JAVA_HOME + "/apache-maven-" + M2_VERSION


# ENV
COREPATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games"
PATH=PYTHONHOME + "/bin" + ":" + JAVA_HOME + "/bin" + M2_HOME + "/bin" + COREPATH


if __name__ == '__main__':
    import os,sys
    # TODO:  modify this for proper variables sys.env
    print "python environment... loaded."
    os.environ["PYTHONHOME"]=PYTHONHOME
    os.environ["PYTHONPATH"]=PYTHONPATH
    os.environ["JAVA_HOME"]=JAVA_HOME
    sys.prefix=PYTHONHOME
    sys.exec_prefix=PYTHONHOME
    sys.path.append(PYTHONHOME)
    sys.path.append(PYTHONPATH)
    os.chdir(PYTHONHOME)

