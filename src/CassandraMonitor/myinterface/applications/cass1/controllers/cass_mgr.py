# coding: utf8
from __future__ import absolute_import
import sys
# total hack
sys.path.append("\
/opt/work/projects/Cassandra-Monitor/src/CassandraMonitor/myinterface/applications/cass1/controllers")

import mydata.data as d

def index():
    data = d.MyData()
    myjmx = data.mydict()
    return dict(myjmx)


