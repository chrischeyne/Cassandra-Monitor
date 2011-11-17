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
this module is the handler for my{jmx,cassandra...} data handlers
"""
import operator
from functional import compose, partial

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"


def main():
    
    # FIXME: only load relevant modules using __ALL__
    # REPLACE WITH AN INIT SYSTEM!
    # def __start(): __stop(whichhandler..)

    import myjmxhandler.jmxhandler
    import mymysqlhandler.sqlhandler

    jmx = myjmxhandler.jmxhandler.Myjmx()
    jmx.boot()
    
    # note add daemon interface in figure
    sql = mymysqlhandler.sqlhandler.Mysql()
    sql.boot()



if __name__ == "__main__":
    main()

