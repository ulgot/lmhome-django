from django.conf.urls import patterns, url

from publications import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<publication_id>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<publication_id>\d+)/vote/$', views.vote, name='vote'),
    )

