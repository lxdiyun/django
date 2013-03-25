from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from gallery.models import Item, Photo

urlpatterns = patterns('django.views.generic',
                       url(r'^$',
                           'simple.direct_to_template',
                           kwargs={
                               'template': 'index.html',
                               'extra_context': {
                                   'item_list': lambda: Item.objects.all()
                               }
                           },
                           name='index'
                           ),
                       url(r'^items/$',
                           ListView.as_view(
                               queryset=Item.objects.all(),
                               context_object_name='items_list',
                               template_name='items_list.html'
                           ),
                           name='item_list'
                           ),
                       url(r'^items/(?P<pk>\d+)/$',
                           DetailView.as_view(
                               model=Item,
                               template_name='items_detail.html',
                           ),
                           name='item_detail'
                           ),
                       url(r'^photos/(?P<pk>\d+)/$',
                           DetailView.as_view(
                               model=Photo,
                               template_name='photos_detail.html',
                           ),
                           name='photo_detail'
                           ),
                       )
