# DIRECTORY STRUCTURE
cassandramanager.py     - boots web2py and all below modules

mycassandramanager/         - core management system

    js/                         - js libraries (usually flot)
    templates/                  - temporary template area for testing django/flot
    db/                         - temporary sqlite db area for testing
    /cacti-templates            - Cassandra 1.x compatible CACTI templates

    mydatagatherer/datagatherer.py      - core gathering 'daemons' manager
    .......myjmxhandler/                 - captures internal JVM JMX info
    .......mymysqlhandler/               - working on this as a side project
    .......mycassandrahandler           - this does more performance-orientated stats
    .......mycassandrahmxhandler/        - this is for internal cassandra JMX info
    .......myjsonhandler/                - JSON manipulation - streams JSON
                                           between tornado/rocket instances


Fri Dec  9 14:50:04 GMT 2011
