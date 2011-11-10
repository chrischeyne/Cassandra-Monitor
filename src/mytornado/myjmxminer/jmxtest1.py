#!/usr/bin/env python2.6
import jpype
from jpype import java
from jpype import javax
import sys

HOST='10.10.1.39'
PORT=7198
USER='admin'
PASS='mypass'

URL = "service:jmx:rmi:///jndi/rmi://%s:%d/jmxrmi" % (HOST, PORT)
#this it the path of your libjvm
# /opt/jdk1.6.0_27/jre/lib/amd64/server/libjvm.so
jpype.startJVM("/System/Library/Frameworks/JavaVM.framework/Libraries/libjvm_compat.dylib")
java.lang.System.out.println("JVM load OK")
sys.exit(1)

jhash = java.util.HashMap()
jarray=jpype.JArray(java.lang.String)([USER,PASS])
jhash.put (javax.management.remote.JMXConnector.CREDENTIALS, jarray);
jmxurl = javax.management.remote.JMXServiceURL(URL)
jmxsoc = javax.management.remote.JMXConnectorFactory.connect(jmxurl,jhash)
connection = jmxsoc.getMBeanServerConnection();


object="java.lang:type=Threading"
attribute="ThreadCount"
attr=connection.getAttribute(javax.management.ObjectName(object),attribute)
print  attribute, attr

#Memory is a special case the answer is a Treemap in a CompositeDataSupport
object="java.lang:type=Memory"
attribute="HeapMemoryUsage"
attr=connection.getAttribute(javax.management.ObjectName(object),attribute)
print attr.contents.get("used")


