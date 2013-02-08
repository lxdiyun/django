from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^mysite/', include('mysite.foo.urls')),

                       # Uncomment the admin/doc line below to enable
                       # admin documentation:
                       url(r'^admin/doc/',
                           include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^gallery/', include('gallery.real_urls')),
                       url(r'^polls/', include('polls.urls')),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^cms/', include('cms.urls')),
                       url(r'^liveupdate/', include('liveupdate.urls')),
                       url(r'^paste/', include('pastebin.urls')),

                       url(r'^pages/',
                           include('django.contrib.flatpages.urls')),
                       )
