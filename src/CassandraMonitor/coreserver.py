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

# Thu Dec  1 15:37:42 GMT 2011
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

import sys
import os
import imp
import mylogger.logger as loggingsystem
SYSLOG = loggingsystem.MyLogger()
SYSLOG.l.debug('booting....')
import myconfig.config as config
SYSCONFIG = config.MyConfig()
SYSLOG.l.info('mysql host is %s ' % SYSCONFIG.conf['mysql']['host'])


# CONFIGURATION HANDLER


def findmodules(path="."):
    """ find modules in path: path """
    modules = set()
    for f in os.listdir(path):
        m = None
        if f.endswith(".py"):
            m = f[:-3]
        if m is not None:
            modules.add(m)
    return list(modules)



def loadmodules(name,path=["."]):
    """ return modules for paths """
    (file,pathname,description) = imp.find_module(name,path)
    return imp.load_module(name,file,pathname,description)

# MAIN LOOP
__all__ = None
def main():

    """ our default bootstrapper. calls each module in turn. """
    """ diagramatically, this is: - """
    __all__ = [loadmodules(name) for name in findmodules()]
    print "ALL IS FULL OF LOVE ",__all__
    sys.exit(1)

    # BOOT AND CONFIGURE TORNADO
    import tornado.httpserver
    import tornado.ioloop
    import tornado.options
    import tornado.web
    
    # FIXME: remap this to import myconfig; myconfig.tornado.port
    from tornado.options import define, options
    define("port", default=8888, help="default to port 8888", type=int)
    tornado.options.parse_command_line()

    # Handlers:  root, cacti, ganglia, flot in graphs, manager
    # TODO: others

    coreserver = tornado.web.Application([
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
