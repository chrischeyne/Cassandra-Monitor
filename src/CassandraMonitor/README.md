# DIRECTORY STRUCTURE

__init__.py
cassandramonitor.py         - core launcher
coredjango.py               - core django handler
coreserver.py               - core tornado http server, and 
corefetcher.py              - core tornado http client launcher, which launch:

plugins/                    - future development area for plugins
mylogger/                   - core logging system logger

mycassandramanager/         - core management system

    graphing/                   - templates for graphing systems (+flot)
    graphs/                     - graph generation system
    js/                         - js libraries (usually flot)
    templates/                  - temporary template area for testing django/flot
    db/                         - temporary sqlite db area for testing

    mydatagatherer/datagatherer.py      - core gathering 'daemons' manager
    .......myjmxhandler/                 - captures internal JVM JMX info
    .......mymysqlhandler/               - working on this as a side project
    .......mycassandrahandle/r           - this does more performance-orientated stats
    .......mycassandrahmxhandler/        - this is for internal cassandra JMX info
    .......myjsonhandler/                - JSON manipulation



Fri Dec  2 15:05:11 GMT 2011
