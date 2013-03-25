from django.conf.urls.defaults import patterns, url, include
from gallery.setting import ROOT_URL


urlpatterns = patterns('',
                       url(r'^%s' % ROOT_URL[1:],
                           include('gallery.real_urls')),
                       )
