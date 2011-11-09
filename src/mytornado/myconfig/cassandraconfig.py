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


#Wed Nov  9 11:24:56 GMT 2011
"""
this is our configuration area. From here we can determine, via YAML, which
variables to operate on; e.g.
cluster 1 has jmx port 7198 but cluster 2 has 7199

also determine where our java and python installs are

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


import yaml

#FIXME: place in cassandraconfig.yaml

document = """

    defaulttornadoport:8181
    defaultcassandrarpc:9160
    defaultcassandrajmx:7199
    defaultcassandrastorage:7000
    defaultcassandramx4j:7197
    myjdk : ['/opt/jdk1.6.0_27']
    mypy : ['/opt/python2.7.2']
    
    # RING 1
    ring1 : ['10.0.0.1','10.0.0.2','10.0.0.3]
    
    # FIXME: r1(jmx,rpc,storage,mx4k,pyjmx..)
    # r2(jmx,rpc,storage,mx4k,pyjmx..) ...


"""
configurationfile='cassandraconfig.yaml'
yaml.load(document)


