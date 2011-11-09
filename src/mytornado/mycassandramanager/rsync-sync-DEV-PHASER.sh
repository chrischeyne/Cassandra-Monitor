#!/usr/bin/env bash

# CASSANDRA SYNC DEFINITION BUBBLE
# FLORENCE-DEV:/opt/cluster-dev -> PHASER:/opt/streaming-dev-live/
# PHASER -> SHRIKE:/opt/cluster-live (via rsync-sync-PHASER-SHRIKE.sh)

# Thu Nov  3 10:01:27 GMT 2011
echo "RSYNC for PYTHON directory in progress..."
source ./CLUSTER_ENVIRONMENT.sh
echo "PYTHON HOME IS ${PYTHONHOME}"
echo "JAVA HOME IS ${JAVA_HOME}"
echo "CASSANDRA AREA IS ${CASSANDRA_HOME} + ${CASSANDRA_CONF} +\
${CASSANDRA_INCLUDE}"

PHASER_LIVE=212.42.3.21
PHASER_PORT=48522
    
echo "Syncing PYTHON-DEV to PHASER LIVE ${PHASER_LIVE}:${PHASER_PORT}..."
rsync -avz --progress --inplace --rsh='ssh -p48522' ${PYTHONHOME}/ \
    root@${PHASER_LIVE}:/opt/streaming-dev-live${PYTHONHOME}


echo "Syncing JAVA-DEV to PHASER LIVE ${PHASER_LIVE}:${PHASER_PORT}..."
rsync -avz --progress --inplace --rsh='ssh -p48522' ${JAVA_HOME}/ \
    root@${PHASER_LIVE}:/opt/streaming-dev-live${JAVA_HOME}


echo "Syncing CASSANDRA-DEV to PHASER LIVE ${PHASER_LIVE}:${PHASER_PORT}..."
# SRC COMPILED DISTRIBUTION
rsync -avz --progress -r -R --inplace --rsh='ssh -p48522' ${CASSANDRA_HOME}/ root@${PHASER_LIVE}:/opt/streaming-dev-live/

# CONFIGURATION AREA
rsync -avz --progress -r -R --inplace --rsh='ssh -p48522' ${CASSANDRA_CONF}/ root@${PHASER_LIVE}:/opt/streaming-dev-live/

# ENVIRONMENT AREA
# rsync -avz --progress -r -R --inplace --rsh='ssh -p48522' ${CASSANDRA_CORE}/ root@${PHASER_LIVE}:/opt/streaming-dev-live/

