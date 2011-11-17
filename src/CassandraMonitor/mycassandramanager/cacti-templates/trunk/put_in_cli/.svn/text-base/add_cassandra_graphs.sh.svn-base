
. cacti_func.sh

host=$1
if [ "$host" = "" ]; then
  echo "argument 0 not specified"
  exit 1
fi

h_id=`getIdForHost "$host" `
if [ "$h_id" = "" ]; then
  echo "Host not found in cacti"
  exit 2
fi

doit=$2

CFs='BrowserData:ColX BrowserData:ColY'
for i in $CFs ; do
  keyspace=`echo $i | cut -d':' -f1`
  columnFamily=`echo $i | cut -d':' -f2`
  wantedGraphs[0]="Cassandra 6.0 db CFStores Read/Write"
  wantedGraphs[1]="Cassandra 6.0 db CFStores Latency"
  wantedGraphs[2]="Cassandra 6.0 db CFStores RowStats"
  wantedGraphs[3]="Cassandra 6.0 db CFStores DiskSpace"
  wantedGraphs[4]="Cassandra 6.0 db CFStores LiveSSTableCount"
  wantedGraphs[5]="Cassandra 6.0 db CFStores PendingTasks"
  wantedGraphs[6]="Cassandra 6.0 db CFStores MemTable"
  wantedGraphs[7]="Cassandra 6.0 db CFStores Latency/Hits"
  cnt=${#wantedGraphs[@]}

  for (( i = 0 ; i < cnt ; i++ ))
  do
    #echo "Element [$i]: ${wantedGraphs[$i]}"
    gt_id=`getIdForGraphTemplate "${wantedGraphs[$i]}" `
    if [ "$gt_id" = "" ] ; then
      echo "Did not find template for ${wantedGraphs[$i]}"
      exit 5
    fi
    title="${host} ${wantedGraphs[$i]} KS=${keyspace} CF=${columnFamily}"
    # number may not be 126 for you.. try this.. php add_graphs.php  --list-input-fields --graph-template-id=132
    inFields=" --input-fields=' 126:port=8585 126:user=dummyUser 126:pass=dummyPass 126:keyspace=${keyspace} 126:columnfamily=${columnFamily}' "
    fullCmd="php add_graphs.php --graph-type=cg --graph-title=\"${title}\" --graph-template-id=${gt_id} ${inFields} --host-id=${h_id} --force "
    echo "$fullCmd"
    if [ ! "$doIt" = "" ] ; then
      `"$fullCmd"`
    fi
  done

  wantedCacheGraphs[0]="Cassandra 6.0 db Caches Sizing"
  wantedCacheGraphs[1]="Cassandra 6.0 db Caches Activity"
  ccnt=${#wantedCacheGraphs[@]}

  for (( i = 0 ; i < ccnt ; i++ ))
  do
    gt_id=`getIdForGraphTemplate "${wantedCacheGraphs[$i]}" `
    if [ "$gt_id" = "" ] ; then
      echo "Did not find template for ${wantedCacheGraphs[$i]}"
      exit 5
    fi
    title="${host} ${wantedCacheGraphs[$i]} KS=${keyspace} CF=${columnFamily}"
    # you may need a number other then 127
    inFields=" --input-fields=' 127:port=8585 127:user=dummyUser 127:pass=dummyPass 127:ks=${keyspace} 127:cf=${columnFamily} ' "
    fullCmd="php add_graphs.php --graph-type=cg --graph-title=\"${title}\" --graph-template-id=${gt_id} ${inFields} --host-id=${h_id} --force"
    echo "$fullCmd"
    if [ ! "$doIt" = "" ] ; then
      `"$fullCmd"`
    fi
  done


done
