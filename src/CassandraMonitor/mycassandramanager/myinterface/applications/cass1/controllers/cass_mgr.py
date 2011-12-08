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

from __future__ import absolute_import
import sys
sys.path.append("/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/myinterface/applications/cass1/controllers")
sys.path.append("/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/myinterface/applications/cass1/controllers/mydata")

import mydata.data as d

def index():
    data = d.MyData()
    myjmx = data.mydict()
    session.counter = (session.counter or 0) + 1
    return dict(myjmx,message="Cass Manager",counter=session.counter)

if __name__ == '__main__':
    data = d.MyData()
    myjmx = data.mydict()
    d = dict(myjmx)
    print d


