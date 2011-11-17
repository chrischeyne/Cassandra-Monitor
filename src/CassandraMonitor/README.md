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

graphing/                   - templates for graphing systems (+flot)
graphs/                     - graph generation system
js/                         - js libraries (usually flot)
mylogger/                   - core logging system logger
templates/                  - temporary template area for testing django/flot
db/                         - temporary sqlite db area for testing


Thu Nov 17 14:27:22 GMT 2011

