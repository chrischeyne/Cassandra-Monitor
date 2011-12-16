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


#Fri Dec 16 09:39:05 GMT 2011
"""
helper class.

functions for sorting out details from data gathering
e.g. sorting dictionaries of JMX results

also returns nodal information for management system

also will implement a class-based inheritence system for different types of
data analysis; including SciPy inparticular


NOTE:  major re-write required; this is mostly a collection of scripts that
operate on generate k,v tuples.

"""

from operator import itemgetter, attrgetter
import os
import fnmatch
import time
import myconfig.config as config
import mylogger.logger as loggingsystem
SYSCONFIG = config.MyConfig()
SYSLOG = loggingsystem.MyLogger()
SYSLOG.l.debug('booting....')



__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"


class MyDataAnalysis():
    """ main monitor object, of type {jmx,perf}Class """
    """ contains sorting methods for returning values """
    """ sorted and ready to stream """
    """ global module """
    # data analysis is a global module
    # so any module can call it
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        pass


    def sortonsecond(a,b):
        """ sorts on a different tuple element """
        return cmp(a[1],b[1])

    def sortbysumvalue(a,b):
        """ a sort function for dictionaries """
        suma = sum(a[1])
        sumb = sum(b[1])
        return cmp(suma,sumb)

    def getkeyvalues(filename='keyvalue.txt'):
        """ get k,v from file filename """
        for line in file(filename):
            key,value = line.split()
            l = d.get(key,[])
            l.append(int(value))
            d[key] = l
        return d

    class Jmxobject:
        """ returns an abstract k,v pair """
        def __init__(self,name,value):
            self.name=name
            self.value=value
        
        def __repr__(self):
            return repr((self.name,self.value))

    class Perfobject:
        """ returns an abstract k,v pair """
        # FIXME: performance analysis. Ideally could clone Jmxobject
        # but leaving separate in case we use a different system
        def __init__(self,name,value):
            pass
        def __repr__(self):
            return repr((self.name,self.value))



    # our list of cassandra jmx k,v pairs for data
    # manipulation
    cassandrajmx = [
            Jmxobject('jmx1',10)
            #FIXME: MORE
            ]

    # our list of cassandra performance k,v pairs
    cassandraperf = [
            Perfobject('perf1',10)
            ]

    # MYSQL PERFORMANCE OBJECTS
    mysqlperformance = [
            Perfobject('perf2',20)
            ]

    def generatorfind(filepat,top):
        for path,dirlist,filelist in os.walk(top):
            for name in fnmatch.filter(filelist,filepath):
                yield os.path.join(path,name)

                # example
                # pyfiles = generatorfind("*.py","/")

    def generatorcat(sources):
        for s in sources:
            for item in s:
                yield item

    def generatorgrep(pat,lines):
        """ match a specific regex to a sequence of lines """
        patc = re.compile(pat)
        for line in lines:
            if patc.search(line): yield line



    def fieldmap(dictseq,name,func):
        """ map specific dict fields through a function """
        for d in dictseq:
            d[name] = func(d[name])
            yield d

    def generatoropen(filenames):
        """ opens compressed mysql/cassandra etc log files """
        for name in filenames:
            if name.endswith("*.gz"):
                yield gzip.open(name)
            elif name.endswith(".bz2"):
                yield bz2.BZ2File(name)
            else:
                yield open(name)

    def follow(myfile):
        """ emulates tail -f """
        myfile.seek(0,2)
        while True:
            line = myfile.readline()
            if not line:
                tine.sleep(0.1)
                continue
            yield line

    def consumequeue(myqueue):
        """ munch a queue, catch the end """
        while True:
            item = myqueue.get()
            if item is StopIteration: break
            yield item

    def getnodes(ring):
        """ return nodes in ring <ring> """
        x = sorted(myconf.conf[ring].values(), key = itemgetter(1))
        return x


if __name__ == '__main__':
    mydata = MyDataAnalysis()
    d = dict(a=1,b=2,c='System',d=40.9)

    mydict = mydata.getkeyvalues(d)
    mygen = mydata.generatorcat(d)
    for i in mygen:
        print i,

# random code to be sorted
# sorted("This is a test string from Me".split(),key=str.lower)
# sorted(student_objects, key=attrgetter('age'))

