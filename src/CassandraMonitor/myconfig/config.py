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

import os
import mylogger.logger as loggingsystem
SYSLOG = loggingsystem.MyLogger()
SYSLOG.l.debug('booting....')


# FIXME: obvious hack must be fixed to point to
# src/myconfig/config.yaml
CONFIG_FILE= os.getcwd() + '/CassandraMonitor/myconfig/config.yaml'
class MyConfig():
    """ returns a configuration holding object """
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.boot()
    
    def boot(self):
        self.configurationfile = CONFIG_FILE
        with open(self.configurationfile) as self.f:
            self.conf = yaml.load(self.f)
            SYSLOG.l.info("self.conf['mysql']['host'] = %s" % \
                     self.conf['mysql']['host'])

    def updateattr(rowkey,colname,value):
        """ important. This updates live running config """
        """ conf.updateattr(ring0,mysqldb,newdatabasename) """
        self.conf['rowkey']['colname'] = value
        # FIXME: write new config file immediately
        # self.f ...
    def dumpconfig(self):
        """ dumps the current running config to stdout """
        print yaml.dump(self.conf,default_flow_style=False)



if __name__ == "__main__":
    myconf = MyConfig()
    myconf.boot()
    print "mysql host" 
    print myconf.conf['mysql']['host']
    print myconf.conf['ring0']['mysqluser']



