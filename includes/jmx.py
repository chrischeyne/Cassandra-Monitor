"""
Ganglia Module to graph JMX values using JPype
Nicolas Brousse <nicolas@brousse.info>
"""
from jpype import *

import os, platform, sys, time

debug = 0

_jmx = None
_jmx_cur_status = {}
_jmx_pre_status = {}
_jmx_pre_time = {}
_eta = 0
_jmx_params = {'User': '',
              'Password': '',
              'Host': '127.0.0.1',
              'Port': '8989',
              'JMXWrapper': '/opt/ganglia/jmxquery.jar'}
    
descriptors = []

gauge_metrics = {}

def Metric_Handler(name):
    global _jmx

    if _jmx is None:
        _jmx = initJVM()

    pre = None
    cur = 0
    eta = 0

    if debug:
        print "[ DEBUG ] _jmx_cur_status length: %d" % len(_jmx_cur_status)
        print "[ DEBUG ] _jmx_pre_status length: %d" % len(_jmx_pre_status)

    if _jmx is None:
        raise TypeError("No valid JMX Object !")

    if name in _jmx_cur_status:
        _jmx_pre_status[name] = _jmx_cur_status[name]

    for d in descriptors:
        if d['name'] == name:
            break

    try:
        if "jmxKeyName" in d:
            key = d['jmxKeyName']
        else:
            key = None

        if debug:
            print "[ DEBUG ] _jmx.output(%s, %s, %s, %s)" % \
                (d['name'], d['jmxObjectName'], d['jmxAttributeName'], key)

        _jmx.ping()
        result = _jmx.output(d['name'], d['jmxObjectName'], d['jmxAttributeName'], key)
    except:
        print "Error: ", sys.exc_info()[1]
        raise

    if result.isdigit():
        if debug: print "[ DEBUG ] %s: %s" % (name, result)
        _jmx_cur_status[name] = result

        cur_time = time.time()
        if name in _jmx_pre_time:
            eta = cur_time - _jmx_pre_time[name]
            if debug:
                print '[ DEBUG ] ETA: %d, Last time: %d, Cur time: %d' % (eta, _jmx_pre_time[name], cur_time)

        _jmx_pre_time[name] = cur_time

    if name in _jmx_cur_status:
        cur = _jmx_cur_status[name]
    else:
        cur = 0
    if len(_jmx_pre_status) > 0 and name in _jmx_pre_status:
        pre = _jmx_pre_status[name]
    else:
        pre = 0
    eta = int(eta)

    if name in gauge_metrics:
        if pre is not None and eta > 0:
            ret = (long(cur) - long(pre)) / eta
        else:
            ret = 0
    else:
        ret = cur

    if debug:
        print "[ DEBUG ] Metric_Handler(%s): %s (eta: %s, cur: %s, pre: %s)" % (name, ret, eta, cur, pre)

    return long(ret)

def Init_Metric (name, jmxObjectName, jmxAttributeName, jmxKeyName, tmax, type, slope, units, fmt, handler):
    '''Create a metric definition dictionary object.'''
    d = {'name': name.lower(),
        'jmxObjectName': jmxObjectName,
        'jmxAttributeName': jmxAttributeName,
        'jmxKeyName': jmxKeyName,
        'call_back': handler,
        'time_max': tmax,
        'value_type': type,
        'units': units,
        'slope': slope,
        'format': fmt,
        'description': 'JMX '+name.replace("_"," "),
	    'groups': 'jmx'}
    return d
    

def metric_init(params):
    global _jmx, _jmx_params

    if debug: print "[ DEBUG ] metric_init()"

    if 'User' in params:
        _jmx_params['User'] = params['User']

    if 'Password' in params:
        _jmx_params['Password'] = params['Password']

    if 'Host' in params:
        _jmx_params['Host'] = params['Host']

    if 'Port' in params:
        _jmx_params['Port'] = int(params['Port'])
    
    if 'JMXWrapper' in params:
        _jmx_params['JMXWrapper'] = params['JMXWrapper']
    
    return descriptors

def initJVM():
    if debug: print "[ DEBUG ] initJVM()"

    if platform.architecture()[0] == "32bit":
        arch="i386"
    else:
        arch="amd64"

    jvm="/usr/java/jdk/jre/lib/%s/client/libjvm.so" % arch
    if not os.path.isfile(jvm):
        jvm="/usr/java/jdk/jre/lib/%s/server/libjvm.so" % arch
        if not os.path.isfile(jvm):
            raise IOError("Can't find the libjvm.so (%s)" % jvm)

    if not os.path.isfile(_jmx_params['JMXWrapper']):
        raise IOError("Can't find the JMX Wrapper at'%s'" % \
            _jmx_params['JMXWrapper'])

    try:
        startJVM(jvm, "-Djava.class.path=%s" % _jmx_params['JMXWrapper'])
        
        url = "service:jmx:rmi:///jndi/rmi://%s:%d/jmxrmi" % \
               (_jmx_params['Host'], int(_jmx_params['Port']))

        JMXQuery = JClass("org.munin.JMXQuery")

        if _jmx_params['Password'] is not '':
            _jmx = JMXQuery(url, username, password)
        else:
            _jmx = JMXQuery(url)

        _jmx.connect()
    except:
        print "Error: ", sys.exc_info()[1]
        raise

    return _jmx

def metric_cleanup():
    '''Clean up the metric module.'''
    #shutdownJVM()

def Build_Conf():
    print "modules {\n module {\n  name = \"jmx\"\n  language = \"python\"\n }\n}\n"
    print "collection_group {\n collect_every = 30\n time_threshold = 60"
    for d in descriptors:
        print " metric {\n  name = \""+d['name']+"\"\n  title = \""+d['description']+"\"\n  value_threshold = 1.0\n }"
    print "}\n"

descriptors.append(
    Init_Metric("java_cpu_time", "java.lang:type=Threading", "CurrentThreadCpuTime", "",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_cpu_user_time", "java.lang:type=Threading", "CurrentThreadUserTime", "",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_memory_nonheap_committed", "java.lang:type=Memory", "NonHeapMemoryUsage", "committed",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_memory_nonheap_max", "java.lang:type=Memory", "NonHeapMemoryUsage", "max",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_memory_nonheap_used", "java.lang:type=Memory", "NonHeapMemoryUsage", "used",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_memory_heap_committed", "java.lang:type=Memory", "HeapMemoryUsage", "committed",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_memory_heap_used", "java.lang:type=Memory", "HeapMemoryUsage", "used",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_memory_heap_max", "java.lang:type=Memory", "HeapMemoryUsage", "max",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("os_memory_physical", "java.lang:type=OperatingSystem", "FreePhysicalMemorySize", "",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("os_memory_vm", "java.lang:type=OperatingSystem", "CommittedVirtualMemorySize", "",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_thread_count", "java.lang:type=Threading", "ThreadCount", "",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))
descriptors.append(
    Init_Metric("java_thread_count_peak", "java.lang:type=Threading", "PeakThreadCount", "",
        int(300), 'uint', 'both', '', '%u', Metric_Handler))

#This code is for debugging and unit testing    
if __name__ == '__main__':
    try:
        if len(sys.argv) <= 1:
            debug = 1

        metric_init(_jmx_params)

        if len(sys.argv) <= 1:
            while True:
                for d in descriptors:
                    v = d['call_back'](d['name'])
                time.sleep(5)
        elif sys.argv[1] == "config":
            Build_Conf()
            metric_cleanup()

    except KeyboardInterrupt:
        print "Process interrupted."
        if _JMX_WorkerThread.running and not _JMX_WorkerThread.shuttingdown:
            _JMX_WorkerThread.shutdown()
        time.sleep(0.2)
        sys.exit(1)
