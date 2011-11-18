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

"""
Tests for 
"""

import logging


__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"


class MyLogger():
    """ returns an instance of the Python logger. """
    """ designed to allow <MYPROGRAMNAME><classinstance><fn><timestamp> """
    """ message type commenture """

    l = None
    def __init__(self):
        self.boot()
    def boot(self):
        """ main boot handler """
        self.l = logging.getLogger('CASSMGR')
        self.l.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        myformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        myformatter = logging.Formatter(myformat)
        ch.setFormatter(myformatter)
        self.l.addHandler(ch)
        self.l.info('logger.py MyLogger() booting')
        
def main():
    SYSLOG = MyLogger()
    SYSLOG.l.warn('BOOTED!')
    
if __name__ == '__main__':
    main()

