#!/usr/bin/env bash


#Thu Nov  3 10:34:41 GMT 2011
#FIXME: make this actually decent in python with map(pad,new)

# CASSANDRA SYNC DEFINITION BUBBLE
# PHASER:/opt/streaming-dev-live/opt/cassandra-dev -> SHRIKE:/opt/cluster-live 


echo "RSYNC for PYTHON directory in progress..."
source ./CLUSTER_ENVIRONMENT.sh

PAD=/opt/streaming-dev-live

echo "PYTHON HOME IS ${PYTHONHOME}"
echo "JAVA HOME IS ${JAVA_HOME}"
echo "CASSANDRA AREA IS ${CASSANDRA_HOME} + ${CASSANDRA_CONF} +\
${CASSANDRA_INCLUDE}"
SHRIKE_LIVE=10.10.1.203
# internal
SHRIKE_PORT=22
    
echo "Syncing PYTHON-DEV to SHRIKE LIVE ${SHRIKE_LIVE}:${SHRIKE_PORT}..."
rsync -avz --progress --inplace --rsh='ssh -p22' ${PAD}/${PYTHONHOME}/ \
    root@${SHRIKE_LIVE}:${PYTHONHOME}


echo "Syncing JAVA-DEV to SHRIKE LIVE ${SHRIKE_LIVE}:${SHRIKE_PORT}..."
rsync -avz --progress --inplace --rsh='ssh -p22' ${PAD}/${JAVA_HOME}/ \
    root@${SHRIKE_LIVE}:${JAVA_HOME}


echo "Syncing CASSANDRA-DEV to SHRIKE LIVE ${SHRIKE_LIVE}:${SHRIKE_PORT}..."
# SRC COMPILED DISTRIBUTION
rsync -avz --progress --inplace --rsh='ssh -p22' ${PAD}/${CASSANDRA_HOME}/ \
    root@${SHRIKE_LIVE}:${CASSANDRA_HOME}


# CONFIGURATION AREA

rsync -avz --progress --inplace --rsh='ssh -p22' ${PAD}/${CASSANDRA_CONF}/ \
    root@${SHRIKE_LIVE}:${CASSANDRA_CONF}


# ENVIRONMENT AREA
# rsync -avz --progress -r -R --inplace --rsh='ssh -p48522' ${CASSANDRA_CORE}/ root@${SHRIKE_LIVE}:/opt/streaming-dev-live/
echo ${PAD}/${CASSANDRA_HOME}
echo ${PAD}/${CASSANDRA_CONF}
echo ${CASSANDRA_HOME}
echo ${CASSANDRA_CONF}


