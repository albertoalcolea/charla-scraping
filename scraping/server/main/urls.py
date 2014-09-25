from django.conf.urls import patterns, include, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^more/$', views.more, name='more'),
)