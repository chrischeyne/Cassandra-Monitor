CACTI_HOME=/var/www/html/cacti
CLI_HOME=/var/www/html/cacti/cli

getIdForHost() {
  host=$1
  res=`php ${CLI_HOME}/add_graphs.php --list-hosts | grep $host | awk '{print $1}'`
  if [ ! "$res" = "" ] ; then
    echo $res
  else
    return 1
  fi
}

getIdForGraphTemplate() {
  template=$1
  res=`php ${CLI_HOME}/add_graphs.php --list-graph-templates | grep "$template" | awk '{print $1}'`
  if [ ! "$res" = "" ] ; then
    echo $res
  else
    return 1
  fi
}
#x=$(getIdForHost xxxxx)
#echo $x

#y=$(getIdForGraphTemplate "Cassandra 6.0 db Caches Activity")
#echo $y
