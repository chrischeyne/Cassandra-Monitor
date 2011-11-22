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
    """ interface to MySQL """

    def __enter__(self):
        """ returns a db object """
        db = MySQLdb.connect(\
            host=SYSCONFIG.conf['mysql']['host'], \
            user=SYSCONFIG.conf['mysql']['user'], \
            passwd=SYSCONFIG.conf['mysql']['pass'])

        return db
    
    def __exit__(self,type,value,traceback):
        return isinstance(value,TypeError)



    def MySQLdbError(e):
        """ raise an mysql exception """
        try:
            print "mysql error"
            #SYSLOG.l.warn("MySQL error [%d]: %s" % (e.args[0],e.args[1]))
        except IndexError:
            print "indexerror"
            #SYSLOG.l.warn("MySQL info : %s" % str(e))
            pass

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

class Mysql():
    """ mysql connection handler that sends out dicts of mysql info """
    def __init__(self):
        # DATABASE HANDLER
        self.db_connection = None
        # OUR K,V PAIRS OF MYSQL INFO
        self.MYSQLDICT = {}
        
    def mysqlkgenerator(self):
        """ throwaway data generator """
        for i in self.MYSQLDICT.keys(): yield i
    
    def _mysqlkvgenerator(self,mydict):
        """ throwaway data generator in 2-D """

        for (i,j) in mydict.keys(),mydict.values(): yield (i,j)

    def _mysqliterator(self,mydict):
        """ iterate over all items and print """
        for i,j in mydict.iteritems(): print i,j
    
    def builddata(self,mydict):
        """ async ticker to pick up new changes """
        """ and populate dictionary """

    def getdata(self):
        """ returns a sorted dict of mysql values """
        self._mysqlkvgenerator(self.MYSQLDICT)


    def boot(self):
        """ main boot class. Initialises MYSQL dict """
        
        self.MYSQLDICT['Bytes_received'] = 2048 
        self.MYSQLDICT['Com_insert'] = 1024
        MYSQL_STATUS_CMD = "show status where variable_name = "
        MYSQL_EXTENDEDSTATUS_PARSER = "mysqladmin extended-status -p" + \
                SYSCONFIG.conf['mysql']['pass'] + "-i1 -r"
        
        #SYSLOG.l.debug('MySQL parser ' , MYSQL_PARSER)

        db_connection = MyDatabaseConnection()
        with db_connection as cursor:
            pass
        print "boot(): finished"

if __name__ == '__main__':
    mysqlhandler = Mysql()
    mysqlhandler.boot()
    print "MYSQL DATA HANDLER..."
    
    # GENERATE(data) <-- http_client() --> tornado()
    # ASYNC
    mysqlhandler.getdata()
    #print "BYTES RECEIVED: " , mysqlhandler.MYSQLDICT['Bytes_received']



 
