from django.conf.urls import patterns, include, url
from tree import views

urlpatterns = patterns('',
	url(r'^node/(?P<pk>\d+)/(?P<name>[A-Za-z0-9\_]+)?', views.ShowNode.as_view(), name='ShowNode'),
)

