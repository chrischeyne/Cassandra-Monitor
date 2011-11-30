from __future__ import absolute_import
import sys
sys.path.append("/opt/work/projects/web2py/applications/cass1/controllers/mydata")

# coding: utf8
# try something lik

import data as d

def index():
    data = d.MyData()
    myjmx = data.mydict()
    return dict(myjmx)


