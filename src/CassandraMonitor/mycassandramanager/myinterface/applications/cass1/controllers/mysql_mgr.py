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

# Fri Dec  9 09:20:50 GMT 2011
"""
Initial testing controller.  Runs 'Cass Perf'
TODO: migrate each class to it's own module to allow for
wide-scale development.  
TODO: expose more variables internally for extension/plugin system
"""

from __future__ import absolute_import
# FIXME: reconfigure paths
import sys
sys.path.append("/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/myinterface/applications/cass1/controllers")
sys.path.append("/opt/cassandra-dev/PROJECTS/Cassandra-Monitor/src/CassandraMonitor/mycassandramanager/myinterface/applications/cass1/controllers/mydata")

import mydata.data as d
import networkx  as nx
import matplotlib.pyplot as plt

# CLASS PAGE HANDLERS - BELOW FOR METHOD HANDLERS

class CassandraPerformance():
    def __init__(self):
        pass
    def _perf1(self):
        """ draw the cluster overview """
        return dict()

    def _generategraph(self):
        """ return a graph of cluster """
        pass
        G=nx.Graph(cluster="ring0live")
        G.add_node(1)
        G.add_nodes_from([2,3])
        H=nx.path_graph(10)
        G.add_nodes_from(H)
        G.add_node(H)
        G.add_edge(1,2)
        e=(2,3)
        G.add_edge(*e)
        nx.draw(G)
        plt.show()
        return G 

    def _admin(self):
        pass


def index():
    data = d.MyData()
    myjmx = data.mydict()
    session.counter = (session.counter or 0) + 1
    return dict(myjmx,message="Cassandra Real-time Performance",counter=session.counter)


def CassandraPerformance():
    """ PAGE:  CASSANDRA PERFORMANCE - OVERVIEW """ 
    cp = CassandraPerformance() 
    d = co._generategraph()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict



