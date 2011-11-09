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


#Wed Nov  9 11:24:56 GMT 2011
"""
This module interfaces to JMX to proide real-time monitoring
it will also instigate tornado daemons

"""

from jpype import *
# FIXME: move to parent
import logging as lg 
import os,platform,sys,time

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

#NOTE: ORIGINAL AUTHORED BY NICOLAS BROUSSE
#FIXME: CREDITS http://is.gd/Wx6UZQ


def metric_cleanup():
    """ shut down the JVM for gc """
    pass

def Build_Conf():
    lg.debug("module listing : - \
           ")
    pass


def boot():
    """ simple boot module to start the lg system
    """

    try:
        if len(sys.argv) <= 1:
            debug = 1
            # initiate our debug printing logger
            lg.basicConfig(level=lg.DEBUG)
            lg.debug('booting jmx')

        metric_init(_jmx_params)
    
        if len(sys.argv) <= 1:
            while True:
                for d in descriptors:
                    v = d['call_back'](d['name'])
                time.sleep(5)

        elif sys.argv[1] == "config":
            Build_Conf()
            metric_cleanup()

    except KeyboardInterrupt:
        lg.debug('KEYBOARD INTERRUPT')
        if _JMX_WorkerThread.running and not _JMX_WOrkerThread.shuttingdown:
            _JMX_Worker_Thread.shutdown()
        tim.sleep(1)
        lg.debug('shutting down')
        raise SystemExit

if __name__ == "__main__":
    boot()


