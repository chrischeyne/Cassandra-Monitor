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

# Wed Nov 30 14:40:24 GMT 2011
"""
this module is the handler for my{jmx,cassandra...} data handlers
"""
import operator
from functional import compose, partial
import mylogger.logger as loggingsystem
SYSLOG = loggingsystem.MyLogger()
SYSLOG.l.debug('booting....')
import myconfig.config as config
SYSCONFIG = config.MyConfig()
SYSLOG.l.info('mysql host is %s ' % SYSCONFIG.conf['mysql']['host'])

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

class DataGatherer():
    def __init__(self):
        self.main()
    

    def main(self):
        
        # FIXME: only load relevant modules using __ALL__
        # REPLACE WITH AN INIT SYSTEM!
        # def __start(): __stop(whichhandler..)

        import myjmxhandler.jmxhandler
        import mymysqlhandler.sqlhandler

        self.jmx = myjmxhandler.jmxhandler.Myjmx()
        self.jmx.boot()
        
        # note add daemon interface in figure
        self.sql = mymysqlhandler.sqlhandler.Mysql()
        self.sql.boot()

if __name__ == "__main__":
    data = DataGatherer()



