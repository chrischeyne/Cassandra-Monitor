#!/usr/bin/python
"""
#do install
sh jdk-6u21-linux-x64.bin 
cp -r jdk1.6.0_21/ /usr/local/
ln -s /usr/local/jdk1.6.0_21/ /usr/local/jdk

export JAVA_HOME=/usr/local/jdk
export PATH=$PATH:$JAVA_HOME/bin

wget wget http://downloads.sourceforge.net/project/jpype/JPype/0.5.4/JPype-0.5.4.1.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fjpype%2Ffiles%2FJPype%2F0.5.4%2F&ts=1291381165&use_mirror=jaist
unzip JPype-0.5.4.1.zip
cd JPype-0.5.4.1

##if install faild path change
####vi setup.py
####vi src/python/jpype/_linux.py

python setup.py install

#do monitring
python get_cassandra_XXX.py #etc...

#check
http://wiki.apache.org/cassandra/JmxInterface
"""

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
    #traceback.print_exc(file=sys.stdout)
    pass
    
class Connect_Error(Error):
    """jmx no connection """
    pass
    
class Attr_Error(Error):
    """jmx do not have attr """
    pass
    
class JAVA(object):
    """start java"""
    def __init__(self,libjvm='/opt/jdk1.6.0_27/jre/lib/amd64/server/libjvm.so'):
        try:
            jpype.startJVM(libjvm)
        except RuntimeError, e:
            traceback.print_exc(file=sys.stdout) 
            #raise JVM_Import_Error(e)
   

class JMX(object):
    """jmx monitor class"""

    def __init__(self, host='127.0.0.1', port=8080, user='cassandra',
                 passwd=''):
             
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.url = "service:jmx:rmi:///jndi/rmi://%s:%d/jmxrmi" % (self.host, self.port)

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
            raise Connect_Error()

        return connection
            
    def get_attr(self,domain,type,attribute):
        """get parameter process memory ..."""

        object = "%s:type=%s" % (domain,type)

        try:
            attr = self.connection.getAttribute(javax.management.ObjectName(object), attribute)

        except:
            raise Attr_Error()

        return attr

if __name__ == '__main__':
    JAVA()
    jmx = JMX()
    print jmx.get_attr('org.apache.cassandra.service', 'StorageService', 'LiveNodes')
    del jmx
