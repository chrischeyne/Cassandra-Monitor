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



#Mon Dec 12 16:47:20 GMT 2011
"""
Implements SimpleJSON handlers
"""
# FIXME: import myconfig
# item[k][v] will come from there



__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"

class MyJSONHandler():
    import requests
    import simplejson as json
    def __init__(self):
        pass

    def getjson(self,url):
        print "url is ",url
        r = self.requests.get(url)
        c = r.content
        j = self.json.loads(c)
        for item in j:
            print item['repository']['url']

    def encodejson(self,data):
        """ return a json object representation of data """
        # FIXME: check separators are correct for yaml dicts
        # s = self.json.dumps(data,separators=(',',':'))
        s = self.json.dumps(data,separators=(',',','))
        return s

    def printjson(self,data):
        s = self.json.dumps(data,sort_keys=True,indent=4 * ' ')
        print '\n'.join([l.rstrip() for l in s.splitlines()])



def main():
    MYJSON = MyJSONHandler()
    # MYJSON.getjson('https://github.com/timeline.json')
    print ' --- '
    mydata = dict(x=12,y=42,a="hello")
    print mydata
    d1 = MYJSON.encodejson(mydata)
    MYJSON.printjson(d1)
    print ' --- '


if __name__ == '__main__':
    main()

