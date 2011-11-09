CASSANDRA MANAGER PROJECT

This project aims to provide a management interface to Cassandra and also delve
deep inside the JMX infrastructure to provide real-time health monitoring of
the Cassandra/JVM internals.  It is also envisioned that there will be a
benchmarking system using statistical theories for schema/data optimisation and
real-time graphing of individual node structures and benchmarks.

Future-bound, it is envisioned that the system will allow deep configuration
of Apache Cassandra similar to say MS-SQL server management studio: -

VISUAL: (inspiration) http://is.gd/sVVXDR

It will be based around a daemon (per node) and a tornado/django (client+server)
idea; however, experimenting with different technologies is the way to go so
far.

tornado + django + flot + ganglia + sshpt + jpype + pyjmx

tornado : non-blocking host for rendering django (mycassandramanager)

mycassandramanager: combining sshpt (or ClusterSsh) for actual node management


torando + httpclient + myjmxhandler ('daemon'-like tool for monitoring local
node but also presenting that

myjmxhandler : using jpype and pyjmx to report in real-time what a node is
doing

mystresshandler : using custom pystress code to stress test a new{ly upgraded}
cluster

flot : real-time graphing; using with tornado+django as a 'web administrator'
tool

ganglia : long-term node monitoring; possibly using cacti instead (as I have
Cassandra cacti templates in src/templates/graphing that are compatible with
1.0-series



Contributors welcome. Brand new pre-alpha project.

chris[[at]]cheynes.org

SEE: live/site/site__links.php

Instigated by Chris Cheyne 01NOV2011:1306
This page modified 

Wed Nov  9 10:46:30 GMT 2011

