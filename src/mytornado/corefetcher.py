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
this is our non-blocking http fetcher that fetches real-time data
from each node or localhost

"""

#FIXME: all of it.
import tornado.ioloop,tornado.httpclient


__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

def handle_request(response):
    if response.error:
        print "gtfo: ", response.error
    else:
        print response.body
    ioloop.IOLoop.instance().stop()

monitorclient = httpclient.AsyncHTTPClient()

#FIXME: we grab a block of JMX statistics from each node, or localhost
monitorclient =fetch("http://www.google.co.uk",handle_request)
ioloop.IOLoop.instance().start()


