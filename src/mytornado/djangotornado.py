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
# django settings must be called before importing models
from django.conf import settings
settings.configure(DATABASE_ENGINE='sqlite3', DATABASE_NAME='mytornado/db/dev.db')
from django import forms
from django.db import models

# FIXME: reference localized python source
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class Message(models.Model):
    """
    Message is the django model class in lorder to use it you will need to
    create the database manually.
    
    sqlite> CREATE TABLE message (id integer primary key, subject varchar(30), content varchar(250));
    sqlite> insert into message values(1, 'subject', 'cool stuff');
    sqlite> SELECT * from message;
    """
    
    subject = models.CharField(max_length=30)
    content = models.TextField(max_length=250)
    class Meta:
        app_label = 'dj'
        db_table = 'message'
    def __unicode__(self):
        return self.subject + "--" + self.content


class DjForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    content = forms.CharField()

class ListMessagesHandler(tornado.web.RequestHandler):
    def get(self):
        messages = Message.objects.all()
        self.render("templates/index.html", title="Cassandra Manager",
                    messages=messages)
        
class FormHandler(tornado.web.RequestHandler):
    def get(self):
        form = DjForm()
        self.render("templates/form.html", title="Cassandra Manager - Forms", form=form)

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
            self.render("templates/form.html", title="Cassandra Manager - Forms", form=form)
            
class mainhandler(tornado.web.RequestHandler):
    def get(self):
        self.write("cassandra manager UP")
        
class CactiHandler(tornado.web.RequestHandler):
    """ handle the cacti pages """
    def get(self):
        self.write("cassandra cacti manager UP")


class GangliaHandler(tornado.web.RequestHandler):
    """ handle the ganglia pages """
    def get(self):
        self.write("cassandra ganglia manager UP")
 
