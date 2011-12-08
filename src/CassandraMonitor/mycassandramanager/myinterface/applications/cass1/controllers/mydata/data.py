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

# Thu Dec  8 10:11:14 GMT 2011
"""
VERY BASIC TEMPORARY TESTING CONTROLLER!!
"""

import logging


__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"
import sys
sys.path.append("/opt/work/projects/web2py/applications/cass1/controllers/mydata")

class MyData():
    def __init__(self):
        self.CASS_JMX = {}
        self.CASS_JMX['Nodetool_Threshold'] = 42
        self.CASS_JMX['JDK_VERSION'] = '1.6.27'
        self.CASS_JMX['CASSANDRA_VERSION'] = 0.86
        self.CASS_JMX['PYTHON_VERSION'] = '2.7.2'
        
    def mydict(self):
        return self.CASS_JMX
 
if __name__ == '__main__':
    data = MyData()
    myjmx = data.mydict()
    print myjmx

   
