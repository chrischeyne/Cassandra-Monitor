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

mainsite/my{*}
mainsite/djangotornado
mainsite/corefetcher 

FIXME: control this from .. main.py (start,stop,restart..) 


"""

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

__all__ = ["mycassandramanager","myconfig","mydataanalysis","mydatagatherer"]

import sys
import os
#import myconfig.config as config
import mylogger.logger as loggingsystem
#SYSCONFIG = config.MyConfig()
SYSLOG = loggingsystem.MyLogger()
SYSLOG.l.info('booting....')


def main():

    """ our default bootstrapper. calls each module in turn. """
    """ diagramatically, this is: - """
 
    # CONFIGURATION HANDLER

    # import mydatagatherer.datagatherer
    # IMPORT DJANGO HANDLER
    # FIXME: import djangotornado as dt
   
    # IMPORT CASSANDRA MANAGER
    # FIXME: import mycassandramanager
    
    # IMPORT CONFIGURATION HANDLER
    # BOOT AND CONFIGURE TORNADO
    import tornado.httpserver
    import tornado.ioloop
    import tornado.options
    import tornado.web
    # FIXME: remap this to import myconfig; myconfig.tornado.port
    from tornado.options import define, options

    define("port", default=8888, help="default to port 8888", type=int)


    tornado.options.parse_command_line()
    coreserver = tornado.web.Application([
        # root, cacti, ganglia, graph (RT graph)
        # TODO: others

        (r"/", dt.ListMessagesHandler),
        (r"/cacti/[0-9]+",dt.CactiHandler),
        (r"/ganglia/[0-9]+",dt.GangliaHandler),
        (r"/form/", dt.FormHandler),
        (r"/graphs/",dt.GraphHandler),


    ])
    
    # launch the 'front page' server
    http_server = tornado.httpserver.HTTPServer(coreserver)
    http_server.listen(options.port)
    # FIXME: terminator on user connection close
    tornado.ioloop.IOLoop.instance().start()


# note we should be called from cassandramonitor.py
if __name__ == "__main__":
    main()
