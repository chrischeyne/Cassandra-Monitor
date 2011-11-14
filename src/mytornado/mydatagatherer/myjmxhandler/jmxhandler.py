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
this module returns dictionarys of data from JVM JMX
these are formatted by ../mydatagatherer/datagatherer

e.g. d = {'heap_size':40000, 'yada':yada, 'jmxyz',42}.dictsort()


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

import re
import sys
import jpype
from jpype import java
from jpype import javax
import traceback


class Error(Exception):
    """Base class for exceptions in this module."""
    pass
    
class JVM_Import_Error(Error):
    """JVM no impor. do find / | grep libjvm.so"""
    traceback.print_exc(file=sys.stdout)
    pass
    
class Erroronconnect(Error):
    """jmx no connection """
    pass
    
class errorAttributes(Error):
    """jmx do not have attr """
    pass
    
class checkjdk(object):
    """start java"""
    def __init__(self,libjvm='/opt/jdk1.6.0_27/jre/lib/amd64/server/libjvm.so'):
        try:
            jpype.startJVM(libjvm)
        except RuntimeError, e:
            raise JVM_Import_Error(e)
   

class JMX(object):
    """jmx monitor class"""
    

    def __init__(self):
        """ boot """
        print "....jmx.JMX()"
        #FIXME: get from myconfig.cassandra
        self.host = 'localhost'
        self.port = 8080
        self.user = 'cassandra'
        self.passwd = ''
        self.url = "service:jmx:rmi:///jndi/rmi://%s:%d/jmxrmi" % (self.host, self.port)
        print self.url

        self.connection = self._connect()

    def __del__(self):
        self.jmxsoc.close()
        
    def _connect(self):
        """make jmx connection"""
        jhash = java.util.HashMap()
        jarray = jpype.JArray(java.lang.String)([self.user,self.passwd])
        jhash.put (javax.management.remote.JMXConnector.CREDENTIALS, jarray);
        jmxurl = javax.management.remote.JMXServiceURL(self.url)

        try:
            self.jmxsoc = javax.management.remote.JMXConnectorFactory.connect(jmxurl,jhash)
            connection = self.jmxsoc.getMBeanServerConnection();

        except:
            raise Erroronconnect()

        return connection
            
    def getattr(self,domain,type,attribute):
        """get parameter process memory ..."""

        object = "%s:type=%s" % (domain,type)

        try:
            attr = self.connection.getAttribute(javax.management.ObjectName(object), attribute)

        except:
            raise errorAttributes()

        return attr

# FIXME: ensure this module can run independently of the 
# manager system

class Myjmx():
    def __init__(self):
        self.name="jmx1"
        
        # what we monitor goes here for i in jmx
        myjmxdict = {}
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'
        myjmxdict['org.apache.cassandra.db'] = 'alpha'

    def returnjmxdata():
        # make thread safe
        return myjmxdict

    def boot(self):
        # test
        checkjdk()
        jmx = JMX()
        print jmx.getattr('org.apache.cassandra.service', 'StorageService', 'LiveNodes')
        del jmx

if __name__ == '__main__':
    jmxhandler = Myjmx()
    jmxhandler.boot()

    
