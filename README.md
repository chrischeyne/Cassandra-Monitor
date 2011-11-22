CASSANDRA MANAGER PROJECT

This project aims to provide a management interface to Cassandra and also delve
deep inside the JMX infrastructure to provide real-time health monitoring of
the Cassandra/JVM internals by polling a python 'bean' attributes.  

It is also envisioned that there will be a
benchmarking system using statistical theories for schema/data optimisation and
real-time graphing of individual node structures and benchmarks.  In other
words, real-time analysis of incoming data; real-time analysis of actual
performance and also integrating (FUTURE) hadoop-based mapreduce system (GUI)

Future-bound, it is envisioned that the system will allow deep configuration
of Apache Cassandra similar to say MS-SQL server management studio: -

VISUAL: (inspiration) http://is.gd/tzDdPw


It will be based around a daemon (per node) and a tornado/django (client+server)
idea; however, experimenting with different technologies is the way to go so
far.

tornado + django + flot + ganglia + sshpt + jpype + pyjmx + pyYAML
(configuration)


tornado : non-blocking host for rendering django (mycassandramanager)
    [tornado <- django(site/dir)]


mycassandramanager: combining sshpt (or ClusterSsh) for actual node management
    # run nodetool on all hosts to compact
    sshpt TOOLS.NODETOOL cluster1 

torando + httpclient + myjmxhandler ('daemon'-like tool for monitoring local
node but also presenting that data to mycassandramanger
    tornado.httpclient(localnode) -> mycassandramanager

myjmxhandler : using jpype and pyjmx to report in real-time what a node is
doing
    myjmxhandler.watchvariables <-- tornado.httpclient (async)


mystresshandler : using custom pystress code to stress test a new{ly upgraded}
cluster
    mycassandramanager.stresstest(cluster1)


flot : real-time graphing; using with tornado+django as a 'web administrator'
tool
    mycassandramanager(sites/flot)


ganglia : long-term node monitoring; possibly using cacti instead (as I have
Cassandra cacti templates in src/templates/graphing that are compatible with
1.0-series
    mycassandramanager(sites/ganglia)

Contributors welcome. Brand new pre-alpha project.  In state of flux.

chris[[#FIXME:remove(at)]]cheynes.org

SEE: live/site/site__links.php

Instigated by Chris Cheyne 01NOV2011:1306
This page modified 


Wed Nov  9 14:13:06 GMT 2011
Tue Nov 22 09:40:08 GMT 2011
