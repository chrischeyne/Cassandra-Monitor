# DIRECTORY STRUCTURE

__init__.py
cassandramonitor.py         - core launcher
coredjango.py               - core django handler
coreserver.py               - core tornado http server 
corefetcher.py              - core tornado http client

....mydatagatherer                  - core gathering 'daemons'
.......myjmxhandler                 - captures internal JVM JMX info
.......mymysqlhandler               - working on this as a side project
.......mycassandrahandler           - this does more performance-orientated stats
.......mycassandrahmxhandler        - this is for internal cassandra JMX info




Thu Nov 17 13:15:20 GMT 2011
