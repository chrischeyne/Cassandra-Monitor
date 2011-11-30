#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
this module returns dictionarys of data from MYSQL DATA
these are formatted by ../mydatagatherer/datagatherer

e.g. d = {'bytes_received':40000, 'yada':yada, 'Com_insert',42}.dictsort()

FIXME: sqlhandler(manager.JmxHandler)
"""


# Wed Nov 30 11:20:24 GMT 2011
__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

# MySQL handler
import MySQLdb
import MySQLdb.cursors
import sys
# FIXME: relocate config modules
import config as config

# FIXME: MERGE BELOW once unit testing complete
#import mylogger.logger as loggingsystem
SYSCONFIG = config.MyConfig()
#SYSLOG = loggingsystem.MyLogger()
#SYSLOG.l.debug('booting....')
#SYSLOG.l.info('mysql host is %s ' % SYSCONFIG.conf['mysql']['host'])

class MyDatabaseConnection():
    """ context manager so we can simply use a with statement """ 
    db = None
    def __init__(self):
        print "MDBC(): connecting to " , SYSCONFIG.conf['mysql']['host']
        self.db = None
        pass

    def cursor(self):
        """ return a cursor """
        try:
            db = MySQLdb.connect(\
                host=SYSCONFIG.conf['mysql']['host'], \
                user=SYSCONFIG.conf['mysql']['user'], \
                passwd=SYSCONFIG.conf['mysql']['pass'])
            
        except MySQLDb.Error, e:
            raise self.MySQLdbError(e)
        else:
            print "cursor() raised connection"
            return db.cursor()
        finally:
            print "cursor().... returned db in else()"

    def __enter__(self):
        """ returns a db object """
        """ basically self.cursor() """
        cursor = self.cursor()
        return cursor 

   
    def __exit__(self,type,value,traceback):
        print "MDBC(): __exit__"
        self.cursor().close
        return isinstance(value,TypeError)
        

    def MySQLdbError(e):
        """ raise an mysql exception """
        try: print "mysql error [%d]: %s" % (e.args[0],e.args[1])
            #SYSLOG.l.warn("MySQL error [%d]: %s" % (e.args[0],e.args[1]))
        except IndexError:
            print "indexerrorMySQL info : %s" % str(e)
            #SYSLOG.l.warn("MySQL info : %s" % str(e))
            pass

class Mysql():
    """ mysql connection handler that sends out dicts of mysql info """
    def __init__(self):
        # iterator counters 
        self.loopcount = 0
        self.GENERATOR_TIMEOUT=1
        self.cursor = None
        # DATABASE HANDLER
        self.db_connection = None
        # 2) MYSQL extended status
        
        MYSQL_ESP = "mysqladmin extended-status -h " \
                + SYSCONFIG.conf['mysql']['host'] \
                + " -u " + SYSCONFIG.conf['mysql']['user'] \
                + " -p " + SYSCONFIG.conf['mysql']['pass']
                # FIXME: iterate on this?  + " -i1 -r"

        MYSQL_CONNECT = "use " + SYSCONFIG.conf['mysql']['db']  + ";"
        # OUR K,V PAIRS OF MYSQL INFO
        # we map this almost as [row_key][colkey][colvalue]
        # from mapping MYSQLCMDS[i] and MYSQLDATA[i][j]
        # initial element is connect to (db listed in myconfig)

        self.MYSQLCMDS=[MYSQL_CONNECT \
                ,SYSCONFIG.conf['mysql']['0comins'] \
                ,SYSCONFIG.conf['mysql']['bytes'] \
                ,SYSCONFIG.conf['mysql']['comdbs'] \
                ,SYSCONFIG.conf['mysql']['comcon'] \
                ]

        # ---
        # MYSQL DATA DICTIONARY
        # 
        # our (k,v) store for MySQL
        #SYSLOG.l.debug('MySQL parser ' , MYSQL_PARSER)
        #FIXME: put in yaml?

        self.MYSQLDATA = {}
        # initialise defaults
        for k in self.MYSQLCMDS:
            self.MYSQLDATA[k]=0
        

    def _mysqliterator(self,mydict):
        """ iterate over all items and print """
        print "_mysqliterator() - STARTING"
        try:
            while True:
                try:
                    for (i,j) in mydict.iteritems():
                        yield i,j
                except Exception, e:
                    yield 'NAN'
        finally:
            print "SQL closing..()"

    def mysqlexecutequery(self,mycursor,mydata,mycmds,myquery,parse=False):
        """ this returns values, so call the generators """
        print "mysqlexecutequery()"
        print mycursor
        print mydata
        print mycmds
        print myquery
        print parse
        print "exqry()  doing query : ",myquery
        mycursor.execute(myquery)
        myresult = mycursor.fetchmany()
        mydata[myquery] = myresult
        print myresult
        if parse: self._mysqliterator(myresult)

    def mysqlquery(self,mycursor,myquery,parse=False):
        """ the anti-deluvian ACME MYSQL QUERY FUNCTION """
        """ parse = parse results; if not Parse -> print results to stdout """
        try:
            print "mysqlquery()"
            print mycursor
            print mydata
            print mycmds
            print myquery
            # boot the query if possible, catch indexerror
            self.mysqlexecutequery(mycursor,myquery,parse)

        except MySQLdb.Error, e:
            # FIXME: proper exception handling
            #raise self.mycursor.MySQLdbError(e)
            print e
           
    def mysqlcommanditerator(self,mycursor,mycmds,mydata):
        """ run through self.MYSQLCMDS and execute each statement """
        """ store the results in self.MYSQLDATA """

        print "=== mysqlcommanditerator() - STARTING ==="
        print mycursor
        print mycmds
        print mydata
        #
        try:
            while True:
                try:
                    for myquery in mycmds.iteritems():
                        self.mysqlexecutequery(mycursor,mycmds,mydata,myquery,True)
                except Exception, e:
                    yield 'NAN'
        finally:
            # FIXME: close properly
            print "CMD closing..()"

    def _mysqlkgenerator(self,mylist):
        """ throwaway data generator """
        for i in mylist:
            yield i

    def _mysqlkvgenerator(self,mydict):
        """ throwaway data generator in 2-D """
        print '_mysqlkvgenerator() dict is'
        print mydict
        #for (i,j) in mydict.keys(),mydict.values(): yield (i,j)

    def printsavedata(self):
        """ use generators above to print all data """
        g2 = self._mysqlkvgenerator(self.MYSQLDATA)
        print "PRINTSAVEDATA():  MYSQL PERFORMANCE DATA"
        print self.MYSQLDATA
        print "PRINTSAVEDATA():  MYSQL CMD DATA"
        print self.MYSQLCMDS

        #print [upper(s) for s in g2.next()]


    def builddata(self,mycursor):
        """ async ticker to pick up new changes """
        """ and populate dictionary """
        """ iterates over MYSQLCMDS """
        print "builddata()"
        print self.MYSQLCMDS
        print self.MYSQLDATA
        self.mysqlcommanditerator(mycursor,self.MYSQLCMDS,self.MYSQLDATA)
        self.loopcount+=1

    def getdata(self,mycursor):
        """ returns a sorted dict of mysql values """
        """ populated from builddata() each tick """
        """ then prints using generators """
        print "getdata():  building...."
        self.builddata(self.mycursor)
        print "getdata():  printing...."
        self.printsavedata()

    def mainloop(self):
        import time
        db_connection = MyDatabaseConnection()
        with db_connection as self.mycursor:
            # whilst we have a connection
            # loop over our dictionaries and populate
            self.getdata(self.mycursor)
            time.sleep(1)
            print self.loopcount

    def boot(self,GENERATOR_TIMEOUT):
        """ args: GENERATOR_TIMEOUT: no of loops/s """
        self.looptimeout = GENERATOR_TIMEOUT
        self.MYSQLDATA = {}
        self.loopcount = 0
        self.mainloop()

if __name__ == '__main__':
    print "RUNNING AS __MAIN___"
    mysqlhandler = Mysql()
    mysqlhandler.boot(1)



 
