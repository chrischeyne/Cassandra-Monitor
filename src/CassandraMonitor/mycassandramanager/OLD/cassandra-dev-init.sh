#!/bin/bash
# chkconfig: 2345 99 01
# description: Cassandra
#   AUTHOR  chris.cheyne@hearst.co.uk
#   REV     0.1A
#   init() for cassandra development; for deployment to /etc/init.d [SYS-V]

# Source fore functions
. /etc/rc.d/init.d/functions
# 

# SOURCE CLUSTER ENVIRONMENT
CORE=/opt/cassandra-dev
source ${CORE}/cluster_config/CLUSTER_ENVIRONMENT.sh

# -------------------------------------------------------------------
echo "CASSANDRA ${CASSANDRA_VERSION} BOOTING"
echo "CLASSPATH $CLASSPATH"
echo "CASSANDRA_HOME $CASSANDRA_HOME"
echo "CASSANDRA_CONF $CASSANDRA_CONF"
echo "CASSANDRA_INCLUDE $CASSANDRA_INCLUDE"
echo "PATH $PATH"

# -------------------------------------------------------------------

echo "Cassandra development binary is $CASSANDRA_BIN"
echo "Cassandra development pid is $CASSANDRA_PID"
echo "Cassandra running $CASSANDRA_BIN $CASSANDRA_YAML_FILE"



if [ ! -f $CASSANDRA_BIN ]; then
  echo "File not found: $CASSANDRA_BIN"
  exit 1
fi

RETVAL=0

start() {
    echo "** init():  STARTING cassandara**" 
    if [ -f $CASSANDRA_PID ] && checkpid `cat $CASSANDRA_PID`; then
    echo "Cassandra is already running."
    exit 0
  fi
  echo -n $"Starting $PROGRAM: "
  exec $CASSANDRA_BIN $CASSANDRA_YAML_FILE -p $CASSANDRA_PID >> $CASSANDRA_LOG 2>&1
  usleep 500000
  RETVAL=$?
  if [ $RETVAL -eq 0 ]; then
    touch $CASSANDRA_LOCK
    echo_success
  else
    echo_failure
  fi
  echo
  return $RETVAL
}

stop() {
  if [ ! -f $CASSANDRA_PID ]; then
    echo "Cassandra is already stopped."
    exit 0
  fi
  echo -n $"Stopping $PROGRAM: "
  
  # FIXME:  re-enable decommission
  # 
  #$CASSANDRA_NODETOOL -h 127.0.0.1 decommission
  #
  
  if kill `cat $CASSANDRA_PID`; then
    RETVAL=0
    rm -f $CASSANDRA_LOCK
    echo_success
  else
    RETVAL=1
    echo_failure
  fi
  echo
  [ $RETVAL = 0 ]
}

get_status() {
  if [ -f $CASSANDRA_PID ] && checkpid `cat $CASSANDRA_PID`; then
    echo "Cassandra is running."
    echo $CASSANDRA_PID
    exit 0
  else
    echo "Cassandra is stopped."
    exit 1
  fi
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
    get_status
    ;;
  restart)
    stop
    start
    ;;
  *)
    echo $"Usage: $PROGRAM {start|stop|restart|status}"
    RETVAL=3
esac

exit $RETVAL
