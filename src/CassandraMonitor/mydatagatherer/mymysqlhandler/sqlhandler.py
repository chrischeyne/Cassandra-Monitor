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
import sys
import config as config


#import mylogger.logger as loggingsystem
SYSCONFIG = config.MyConfig()
#SYSLOG = loggingsystem.MyLogger()
#SYSLOG.l.debug('booting....')
#SYSLOG.l.info('mysql host is %s ' % SYSCONFIG.conf['mysql']['host'])

class MyDatabaseConnection():
    """ context manager so we can simply use a with statement """ 
    def __init__(self):
        print "MDBC(): connecting to " , SYSCONFIG.conf['mysql']['host']
        pass

    def cursor(self):
        """ return a cursor """
        db = MySQLdb.connect(\
            host=SYSCONFIG.conf['mysql']['host'], \
            user=SYSCONFIG.conf['mysql']['user'], \
            passwd=SYSCONFIG.conf['mysql']['pass'])
        # FIXME: proper error handling!!
        # Tue Nov 22 11:45:58 GMT 2011
        # try: yield: finally
        yield db
    
    def __enter__(self):
        """ returns a db object """
        """ basically self.cursor() """
        cursor = self.cursor()
        return cursor

   
    def __exit__(self,type,value,traceback):
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

        # DATABASE HANDLER
        self.db_connection = None
        # OUR K,V PAIRS OF MYSQL INFO
        # initialise empty dictionary
        self.MYSQLDICT = {}

        # QUERY HANDLERS
        # 1) MYSQL EXTENDED STATUS
        MYSQL_STATUS_CMD = "show status where variable_name = "
        MYSQL_ESP = "mysqladmin extended-status -p" + \
                SYSCONFIG.conf['mysql']['pass'] + "-i1 -r"

        # OUR LIST OF ALL MYSQL CMDS ABOVE
        self.ALLCMDS_=['MYSQL_ESP','MYSQL_STATUS_CMD']


    def mysqlquery(mycursor,myquery='SELECT * FROM *'):
        """ the anti-deluvian ACME MYSQL QUERY FUNCTION """
        try:
            # boot the query if possible, catch indexerror
            mycursor.execute(myquery)
        except MySQLDb.Error, e:
            raise MySQLdbError
            
    def mysqlexecutequery(mycursor,myquery="SELECT * FROM *"):
        """ this returns values, so call the generators """
        mycursor.execute(myquery)
        result = cursor.fetchmany()
        # FIXME: in future call the generators for real-time display
        # FIXME: also call dataanalysis.sorted()
        mysqliterator(result)


    def mysqlcommand(self,cmd):
        """ parse the cmd cmd using a parser for that command and update """
        """ self.MYSQLDICT """
       
    def mysqlkgenerator(self):
        """ throwaway data generator """
        for i in self.MYSQLDICT.keys(): yield i
    
    def _mysqlkvgenerator(self,mydict):
        """ throwaway data generator in 2-D """
        print "_mysqlkvgenerator(): dict of len ", len(mydict)
        for (i,j) in mydict.keys(),mydict.values(): yield (i,j)

    def _mysqliterator(self,mydict):
        """ iterate over all items and print """
        print "mysqliterator() length of dict is " , len(mydict) 
        for i,j in mydict.iteritems(): print i,j
    
    def builddata(self,mydict):
        """ async ticker to pick up new changes """
        """ and populate dictionary """
        """ iterates over ALLCMDS """
        # iterator for it.next()
        it = iter(self.ALLCMDS)

    def getdata(self):
        """ returns a sorted dict of mysql values """
        """ populated from builddata() each tick """

        print "getdata():  iterating display.."
        #return self._mysqlkvgenerator(self.MYSQLDICT)
        self._mysqliterator(self.MYSQLDICT)
        #print "getdata():  generating display.."
        #self._mysqlkvgenerator(self.MYSQLDICT)

    def boot(self,GENERATOR_TIMEOUT):
        """ main boot class. Initialises MYSQL dict """
        # FIXME: in yaml file?
        #Tue Nov 22 11:18:09 GMT 2011
        self.looptimeout = GENERATOR_TIMEOUT
        self.loopcount = 0
       
        # our (k,v) store for MySQL
        # populate with default values initially
        # ---
        self.MYSQLDICT['Bytes_received'] = 2048 
        self.MYSQLDICT['Com_insert'] = 1024
        # ---

        #SYSLOG.l.debug('MySQL parser ' , MYSQL_PARSER)

        # connect to database
        db_connection = MyDatabaseConnection()
        # main loop
        # iterate over each __ALL__ and
        # populate our MYSQDICT. Iterator in builddata()

        with db_connection as cursor:
            self.builddata(self.MYSQLDICT)
        print "boot(): finished"

if __name__ == '__main__':
    mysqlhandler = Mysql()
    # FIXME: get the 1 second loop factor from config.yaml?
    mysqlhandler.boot(1)
    print "MYSQL DATA HANDLER..."
    # GENERATE(data) <-- http_client() --> tornado()
    # ASYNC
    mysqlhandler.getdata()



 
