from django.conf.urls.defaults import patterns, include, url

# admin section
from django.contrib import admin
admin.autodiscover()

# url regex
urlpatterns = patterns('',

    url(r'^polls/$','polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$','polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$','polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$','polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
