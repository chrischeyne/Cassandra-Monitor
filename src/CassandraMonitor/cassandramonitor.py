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
main imports core*.py and performs any clean-up upon their termination
"""
__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

__all__ = ["coreserver","mydatagatherer","myconfig","mylogger"]

import sys
import os

# GLOBAL OBJECTS
global SYSCONFIG
global SYSLOG

# FIXME: get rid of this once packaging begins
currentfolder = os.path.dirname(os.path.abspath(__file__))
if currentfolder not in sys.path: sys.path.insert(0,currentfolder)

import coreserver as cs
import myconfig.config as config
import mylogger.logger as loggingsystem
SYSCONFIG = config.MyConfig()
SYSLOG = loggingsystem.MyLogger()
# boot data gathering subsystem
# boot the main handler for all modules 
SYSLOG.l.debug('CORE SERVER BOOTING....')
cs.main()






