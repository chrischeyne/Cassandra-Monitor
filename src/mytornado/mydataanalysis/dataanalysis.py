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

# from import

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

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
    # FIXME: performance analysis
    def __init__(self,name,value):
        pass:

# our list of cassandra jmx k,v pairs
cassandrajmx = [
        Jmxobject('jmx1',10)
        #FIXME: MORE
        ]

# our list of cassandra performance k,v pairs
cassandraperf = [
        Perfobject('perf1',10)
        ]


# random code to be sorted
# sorted("This is a test string from Me".split(),key=str.lower)


