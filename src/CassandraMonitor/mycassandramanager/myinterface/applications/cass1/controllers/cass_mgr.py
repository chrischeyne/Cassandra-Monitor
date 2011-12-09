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
Initial testing controller.  Runs 'Cass Mgr'
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

class ClusterOverview():
    def __init__(self):
        pass
    def _clusteroverview(self):
        """ draw the cluster overview """
        return dict()

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
        """ draw current node overview """
        return dict()

    def _admin(self):
        pass

class KeyspaceManagement():
    def __init__(self):
        pass
    def _clusteradministration(self):
        """ modify the current keyspace / select keyspace """ 
        return dict()

    def _admin(self):
        pass


class DataManagement():
    def __init__(self):
        pass
    def _clusteradministration(self):
        """ visualise the data held in current keyspace """
        return dict()

    def _admin(self):
        pass


# METHOD HANDLERS


def index():
    data = d.MyData()
    myjmx = data.mydict()
    session.counter = (session.counter or 0) + 1
    return dict(myjmx,message="Cass Manager",counter=session.counter)

def first():
    return dict()

def second():
    return dict()



def clusteradministration():
    """ PAGE:  CLUSTEROVERVIEW  """
    co = ClusterAdministration()
    d = co._generategraph()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict


def nodeadministration(): 
    """ PAGE: NODE ADMINISTRATION """
    na = NodeAdministration()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict

def keyspacemanagement(): 
    """ PAGE:  KEYSPACE ADMINISTRATION """
    ks = KeyspaceManagement()
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict

def datamanagement(): 
    """ PAGE:  DATA MANAGEMENT """ 
    dm = DataManagement() 
    #return d
    mydict = dict(a=1,b=2,cluster='RING0LIVE')
    return mydict


# TESTING (learning from web2py.com/book)
def ajaxwiki():
        form=FORM(TEXTAREA(_id='text',_name='text'),
                 INPUT(_type='button',_value='markmin',
                       _onclick="ajax('ajaxwiki_onclick',['text'],'html')"))
        return dict(form=form,html=DIV(_id='html'))

def ajaxwiki_onclick():
    return MARKMIN(request.vars.text).xml()

def rss(url='http://rss.slashdot.org/Slashdot/slashdot/to'):
    """ read and display RSS feed from url <url>"""
    import datetime
    import gluon.contrib.rss2 as rss2
    import gluon.contrib.feedparser as feedparser
    d= feedparser.parse(url)
    d = feedparser.parse("")
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
    """ this page handles <> """
    mydict = dict(a=12,b='page...')
    return mydict

if __name__ == '__main__':
    data = d.MyData()
    myjmx = data.mydict()
    d = dict(myjmx)
    print d


