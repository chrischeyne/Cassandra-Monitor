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
core management server.  Handles: -

mainsite/factory
mainsite/daemongatherer

"""

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

# FIXME: reference localized python source
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

# FIXME: remap this to import myconfig; myconfig.tornado.port

define("port", default=8888, help="default to port 8888", type=int)


class mainhandler(tornado.web.RequestHandler):
    def get(self):
        self.write("cassandra manager UP")
        
class cactihandler(tornado.web.RequestHandler):
    """ handle the cacti pages """
    def get(self):
        self.write("cassandra cacti manager UP")

class gangliahandler(tornado.web.RequestHandler):
    """ handle the ganglia pages """
    def get(self):
        self.write("cassandra ganglia manager UP")
 

def main():
    """ handle the homepage """
    """ boot the handlers """

    ROOT = os.path.normpath(os.path.dirname(__file__))

    tornado.options.parse_command_line()
    application = tornado.web.Application([
        # root, cacti, ganglia
        # TODO: others
        (r"/", mainhandler),
        (r"/cacti/[0-9]+",cactihandler),
        (r"/ganglia/[0-9]+",gangliahandler),
    ])
    
    # launch the 'front page' server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    # FIXME: terminator on user connection close
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
