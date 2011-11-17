#!/usr/bin/env bash
echo "RSYNC for PYTHON directory in progress..."
source ./CLUSTER_ENVIRONMENT.sh
echo "PYTHON HOME IS ${PYTHONHOME}/"


for i in 40 43 50
do
    echo "Syncing PYTHON to 10.10.1.$i"
    rsync -avz --progress -e ssh ${PYTHONHOME}/ \
        root@10.10.1.$i:${PYTHONHOME}/

done


