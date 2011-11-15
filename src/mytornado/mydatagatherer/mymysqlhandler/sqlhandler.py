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


"""

# from import

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

import MySQLdb
# FIXME: from myconfig import mysqlconfig


class Mysql():
    def __init__(self):
        # FIXME: this ain't 2001
        self.name="mysql1"
        self.dbuser='chris'
        self.dbpass='Free1Kick'
        self.db='chris'
        self.server='florence'
        
        #FIXME: more
        MYSQLDICT = {}
        MYSQLDICT['Bytes_received'] = 0
        MYSQLDICT['Com_insert'] = 0


    def mysqlkgenerator():
        """ throwaway data generator """
        for i in MYSQLDICT.keys(): yield i
    
    def mysqlkvgenerator(mydict):
        """ throwaway data generator in 2-D """

        for (i,j) in mydict.keys(),mydict.values(): yield (i,j)

    def mysqliterator(mydict):
        """ iterate over all items and print """
        for i,j in mydict.iteritems(): print i,j


    def boot(self):
        #FIXME: subclass this. All of it.
        #Tue Nov 15 14:41:42 GMT 2011
        MYSQL_STATUS_CMD = "show status where variable_name = "
        MYSQL_PARSER="mysqladmin extended-status -p" . MYCONFIG.MYSQLPASS + \
                "-i1 -r"
         
        db = MySQLdb.connect(host="florence",user="root",passwd="secret")
        MYCURSOR = db.cursor()
        #Tue Nov 15 12:13:02 GMT 2011
        mysql = Mysql()
        self._printsqldata()
        del jmx

def MySQLdbError(e):
    """ raise an sql exception """
    try:
        debug.logger("MySQL error [%d]: %s" % (e.args[0],e.args[1]))
    except IndexError:
        debug.info("MySQL info : %s" % str(e)


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


if __name__ == '__main__':
    mysqlhandler = Mysql()
    mysqlhandler.boot()
    print "MYSQL DATA HANDLER..."
    # GENERATE(data) <-- http_client() --> tornado()
    # ASYNC

    mysqlhandler._printsqldata()



 
