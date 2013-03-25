from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

urlpatterns = patterns('',
#                       url(r'^admin/(.*)', admin.site.root),
                       url(r'^', include('gallery.items.urls')),
                       )
