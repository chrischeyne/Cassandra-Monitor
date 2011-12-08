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
import networkx  as nx
import matplotlib.pyplot as plt
def index():
    data = d.MyData()
    myjmx = data.mydict()
    session.counter = (session.counter or 0) + 1
    return dict(myjmx,message="Cass Manager",counter=session.counter)

def first():
    return dict()

def second():
    return dict()

class ClusterOverview():
    def __init__(self):
        pass
    def _clusteroverview(self):
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


class ClusterAdministration():
    def __init__(self):
        pass
    def _clusteradministration(self):
        """ draw the cluster overview """
        return dict()

    def _admin(self):
        pass
class NodeInformation():
    def __init__(self):
        pass
    def _clusteradministration(self):
        """ draw the cluster overview """
        return dict()

    def _admin(self):
        pass
class KeyspaceManagement():
    def __init__(self):
        pass
    def _clusteradministration(self):
        """ draw the cluster overview """
        return dict()

    def _admin(self):
        pass
class DataManagement():
    def __init__(self):
        pass
    def _clusteradministration(self):
        """ draw the cluster overview """
        return dict()

    def _admin(self):
        pass




def clusteroverview():
    """ CLUSTEROVERVIEW PAGE """
    co = ClusterOverview()
    d = co._generategraph()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict


def clusteradministration():
    """ CLUSTER ADMINISTRATION PAGE """
    co = ClusterAdministration()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict

def keyspacemanagement(): 
    """ CLUSTER ADMINISTRATION PAGE """
    co = ClusterAdministration()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict

def datamanagement(): 
    """ CLUSTER ADMINISTRATION PAGE """
    co = ClusterAdministration()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict


def ajaxwiki():
        form=FORM(TEXTAREA(_id='text',_name='text'),
                 INPUT(_type='button',_value='markmin',
                       _onclick="ajax('ajaxwiki_onclick',['text'],'html')"))
        return dict(form=form,html=DIV(_id='html'))

def ajaxwiki_onclick():
    return MARKMIN(request.vars.text).xml()



def rss():
    import datetime
    import gluon.contrib.rss2 as rss2
    import gluon.contrib.feedparser as feedparser
    d = feedparser.parse("http://rss.slashdot.org/Slashdot/slashdot/to")
    rss = rss2.RSS2(title=d.channel.title,
            link = d.channel.link,
            description = d.channel.description,
            lastBuildDate = datetime.datetime.now(),

            items = [
                rss2.RSSItem(
                    title = entry.title,
                    link = entry.link,
                    description = entry.description,
                    pubDate=datetime.datetime.now()) for entry in d.entries]
                )

    response.headers['Content-Type']='application/rss+xml'
    return rss2.dumps(rss)


def page():
    mydict = dict(a=12,b='RSS FEED')
    return mydict

def page():
    mydict = dict(a=12,b='RSS FEED')
    return mydict

def page():
    mydict = dict(a=12,b='RSS FEED')
    return mydict

def page():
    mydict = dict(a=12,b='RSS FEED')
    return mydict



if __name__ == '__main__':
    data = d.MyData()
    myjmx = data.mydict()
    d = dict(myjmx)
    print d


