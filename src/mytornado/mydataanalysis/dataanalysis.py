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
functions for sorting out details from data gathering
e.g. sorting dictionaries of JMX results
"""

from operator import itemgetter, attrgetter
import os
import fnmatch


__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"


class MONITOROBJECT():
    """ main monitor object, of type {jmx,perf}Class """
    """ contains sorting methods for returning values """
    """ sorted and ready to stream """
    def __init__(self,name):
        # FIXME: this structure will look at follows: -
        # MONITOROBJECT
        # .... name (e.g. ring0node3)
        # .... dictionary of jmxobjects if exist
        # .... dictionary of perfobjects if exist
        # .... timestamp of update
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



# our list of cassandra jmx k,v pairs
cassandrajmx = [
        Jmxobject('jmx1',10)
        #FIXME: MORE
        ]

# our list of cassandra performance k,v pairs
cassandraperf = [
        Perfobject('perf1',10)
        ]

# MYSQL PERFORMANCE OBJECTS
mysqlper


def generatorfind(filepat,top):
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepath):
            yield os.path.join(path,name)

            # example
            #pyfiles = generatorfind("*.py","/")

def generatorcat(sources):
    for s in sources:
        for item in s:
            yield item

def generatorgrep(pat,lines):
    patc = re.compile(pat)
    for line in lines:
        if patc.search(line): yield line



def fieldmap(dictseq,name,func):
    """ map specific dict fields through a function """
    for d in dictseq:
        d[name] = func(d[name])
        yield d



# random code to be sorted
# sorted("This is a test string from Me".split(),key=str.lower)
# sorted(student_objects, key=attrgetter('age'))

