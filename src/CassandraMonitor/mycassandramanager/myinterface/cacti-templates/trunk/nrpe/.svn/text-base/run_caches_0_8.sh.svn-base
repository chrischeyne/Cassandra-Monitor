#java -cp /usr/lib64/nagios/plugins/cassandra-cacti-m6.jar com.jointhegrid.m6.cassandra.CFStores service:jmx:rmi:///jndi/rmi://<host>:<port>/jmxrmi <user> <pass> org.apache.cassandra.db:columnfamily=<columnfamily>,keyspace=<keyspace>,type=ColumnFamilyStores

java -cp /usr/lib64/nagios/plugins/cassandra-cacti-m6.jar com.jointhegrid.hadoopjmx.JMXToolkit -a query -u service:jmx:rmi:///jndi/rmi://${1}:${2}/jmxrmi -c ${3} -p ${4} -o org.apache.cassandra.db:cache=${5},keyspace=${6},type=Caches

