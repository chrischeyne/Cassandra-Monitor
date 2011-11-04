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
__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"


"""

boots the tornado application server and our django test application

"""
# FIXME: reference by module above

import sys,os

import tornado.httpserver, tornado.ioloop, tornado.web

from django.conf import settings
# configure the database connection
# FIXME: use cassandra itself? -chris
# FROM: http://is.gd/CcOIDU
# FIXME: cassandra engine http://is.gd/ZKXbMV
settings.configure(DATABASE_ENGINE='sqlite3',DATABASE_NAME='db/dev.db')

from django import forms
from django.db import models

class Message(models.Model):
    """ base model class
    """

    subject = models.CharField(max_length=30)
    content = models.TextField(max_length=250)

    class Meta:
        app_label = 'dj'
        db_table = 'message'

    def __unicode__(self):
        return self.subject + "--" + self.content

# form definition

class DjForm(forms.Form):
    subject = forms.CharField(max_length=100,required=True)
    content = forms.CharField()

# url handler

class ListMessagesHandler(tornado.web.RequestHandler):
    def get(self):
        messages = Message.objects.all()
        self.render("templates/index.html",title="Cassandra Manager",
                messages=messages)

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        form = DjForm()
        self.render("templates/form.html",title="Form1",form=form)

    def post(self):
        data = {
                'subject':self.request.arguments['subject'][0],
                'content':self.request.arguments['content'][0],
                }

        form = DjForm(data=data)

        if form.is_valid():
            message = Message(**form.cleaned_data)
            message.save()
            self.redirect('/')
        else:
            self.render("templates/form.html",title="form1",form=form)

# url mapper - here we go

cassandramanager = tornado.web.Application( [
    (r"/",ListMessagesHandler),
    ("/form/",FormHandler),
    ] )

def main():
    http_server = tornado.httpserver.HTTPServer(cassandramanager)
    # FIXME: import configuration
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()




