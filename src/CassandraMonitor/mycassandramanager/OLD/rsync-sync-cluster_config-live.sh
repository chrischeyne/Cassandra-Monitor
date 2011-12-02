#!/usr/bin/env bash
#
# this will sync the cluster environment variables in LIVE


echo "RSYNC for CLUSTER_CONFIG **live** directory in progress..."
source ./CLUSTER_ENVIRONMENT-LIVE.sh
echo "CLUSTER CONF IS ${CLUSTER_CONF}/"

# DC0:RAC1 and DC1:RAC1 (223, 225)

for i in 40 47 49 223 225

do
    echo "Syncing LIVE cluster_config to 10.10.1.$i"
    rsync -avz --progress -e ssh ${CLUSTER_CONF}/ \
        root@10.10.1.$i:${CLUSTER_CONF}/

done


