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

# FIXME: MERGE BELOW
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
        # QUERIES
        # 1) MYSQL status with variable 
        # 2) MYSQL extended status
        MYSQL_ESP = "mysqladmin extended-status -p" + \
                SYSCONFIG.conf['mysql']['pass'] + "-i1 -r"
        
        # OUR K,V PAIRS OF MYSQL INFO
        # initialise empty dictionary
        # we map this almost as [row_key][colkey][colvalue]
        # from mapping ALLCMDS[i] and MYSQLDICT[i][j]
        # OUR LIST OF ALL MYSQL CMDS ABOVE
        # This is configured to allow dynamic generation from YAML 
        self.ALLCMDS=[MYSQL_ESP \
                ,SYSCONFIG.conf['mysql']['comins'] \
                ,SYSCONFIG.conf['mysql']['bytes'] \
                ]
        self.MYSQLDICT = {}

    def mysqlexecutequery(mycursor,myquery="SELECT * FROM *"):
        """ this returns values, so call the generators """
        mycursor.execute(myquery)
        result = cursor.fetchmany()
        self._mysqliterator(result)

    def mysqlquery(mycursor,myquery='SELECT * FROM *'):
        """ the anti-deluvian ACME MYSQL QUERY FUNCTION """
        try:
            # boot the query if possible, catch indexerror
            self.mysqlexecutequery(mycursor,myquery)
        except MySQLDb.Error, e:
            raise MySQLdbError
            
    def _mysqlcommanditerator(self,mydict):
        """ parse the cmd cmd using a parser for that command and update """
        """ self.MYSQLDICT """
        """ atm simply runs through ALL.keys() """
        print "_mysqlcommanditerator() - STARTING"
        try:
            while True:
                try:
                    for i in mydict.iteritems():
                        yield i
                except Exception, e:
                    yield 'NAN'
        finally:
            #FIXME: run close
            print "CMD closing..()"
    
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

    def _mysqlkgenerator(self,mylist):
        """ throwaway data generator """
        for i in mylist:
            yield i
    
    def _mysqlkvgenerator(self,mydict):
        """ throwaway data generator in 2-D """
        #print "_mysqlkvgenerator(): dict of len ", len(mydict)
        for (i,j) in mydict.keys(),mydict.values(): yield (i,j)

      
        
    def printdata(self):
        """ use generators above to print all data """
        g1 = self._mysqlkgenerator(self.ALLCMDS)
        g2 = self._mysqlkvgenerator(self.MYSQLDICT)
        # print in format 
        # ALLCMDS[i],MYSQLDICT[j,k]
        for i in g1:
            print "CMD ",i
            for j,k in g2:
                print "....(K,V) ", (j,k)


    def builddata(self):
        """ async ticker to pick up new changes """
        """ and populate dictionary """
        """ iterates over ALLCMDS """

        # iterate over each of ALLCMDS, executing them
        # one-by-one, and updated mydict = self.MYSQLDICT{}

        # loop through all commands foreach tick

        for i in self.ALLCMDS:
            print i

        # update current loop
        self.loopcount+=1
            

    def getdata(self):
        """ returns a sorted dict of mysql values """
        """ populated from builddata() each tick """

        print "COMMANDS, DATA"
        self.builddata()

    def boot(self,GENERATOR_TIMEOUT):
        """ main boot class. Initialises MYSQL dict """
        # FIXME: put data dictionary in YAML file?
        #Tue Nov 22 11:18:09 GMT 2011
        # generator timeout is number of iterations/sec
        self.looptimeout = GENERATOR_TIMEOUT
        self.loopcount = 0
      
        # ---
        # MYSQL DATA DICTIONARY
        # 
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
            self.builddata(self.ALLCMDS)

if __name__ == '__main__':
    print "RUNNING AS __MAIN___"
    mysqlhandler = Mysql()
    # FIXME: get the 1 second loop factor from config.yaml?
    mysqlhandler.boot(1)
    mysqlhandler.getdata()



 
