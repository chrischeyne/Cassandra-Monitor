#!/usr/bin/env bash
echo "RSYNC for JAVA directory in progress..."
source ./CLUSTER_ENVIRONMENT.sh
echo "JAVA HOME IS ${JAVA_HOME}/"


for i in 40 43 50
do
    echo "Syncing JAVA to 10.10.1.$i"
    rsync -avz --progress -e ssh ${JAVA_HOME}/ \
        root@10.10.1.$i:${JAVA_HOME}/

done


