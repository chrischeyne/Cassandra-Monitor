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

THIS IS A TEMPORARY CLASS FOR DEBUGGING

purely boots CassandraMonitor/cassandramonitor.py

FIXME: update for gc and other requriements 
FIXME: change name from __init__
FIXME: this should be a handler to control Exceptions in mytornado 

"""


__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

print "CASSANDRA MONITOR VERSION " + __version__  + " booting..."
print __copyright__
print __maintainer__


# fixme: some init-style scripting here
#
# boot the core handler
from CassandraMonitor.cassandramonitor import main as boot
boot.main()




