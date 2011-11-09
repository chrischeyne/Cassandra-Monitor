#!/usr/bin/env bash
echo "RSYNC for CASSANDRA_CONFIG directory in progress..."
source ./CLUSTER_ENVIRONMENT.sh
echo "CLUSTER CONF IS ${CASSANDRA_CONF}/"


for i in 40 43 50
do
    echo "Syncing cluster_config to 10.10.1.$i"
    rsync -avz --progress -e ssh ${CASSANDRA_CONF}/ \
        root@10.10.1.$i:${CASSANDRA_CONF}/

done


