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
Tests for 
"""

# from import

__author__ = "Chris T. Cheyne"
__copyright__ = "Copyright 2011, The Cassandra Manager Project"
__credits__ = ["Chris Cheyne"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Chris T. Cheyne"
__email__ = "maintainer@cassandra-manager.org"
__status__ = "Alpha"


from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    # some more


class PollAdmin(admin.ModelAdmin):
    list_display=('question','pub_date','was_published_today')

    fieldsets = [
            (None, {'fields':['question']}),
            ('Date information',
                {'fields':['pub_date'],'classes':['collapse']}),
            ]
    inlines = [ChoiceInline]

    list_filter=['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'



def was_published_today(self):
    return self_date.date() == datetime.date.today()

was_published_today.short_description = 'Published today?'
admin.site.register(Poll,PollAdmin)



