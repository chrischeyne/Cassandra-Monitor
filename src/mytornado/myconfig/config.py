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



# Tue Nov 15 17:45:41 GMT 2011
"""
this is our configuration area. From here we can determine, via YAML, which
variables to operate on; e.g.
cluster 1 has jmx port 7198 but cluster 2 has 7199

also determine where our java and python installs are

"""
import yaml



__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

class MyConfig():
    def __init__(self):
        self.configurationfile='config.yaml'
        print "MyConfig() instigated"
    def boot(self):
        self.f = open(self.configurationfile)
        self.conf = yaml.load(self.f)
        self.f.close()
        print "dumping config...."
        print yaml.dump(self.conf,default_flow_style=False)

if __name__ == "__main__":
    myconf = MyConfig()
    myconf.boot()
    print "mysql host" 
    print myconf.conf['mysql']['host']
    print myconf.conf['ring0']['mysqluser']


