from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from tree import views

urlpatterns = patterns('',
	url(r'^node/(?P<pk>\d+)/$', views.ShowNode.as_view(), name='ShowNode'),
	url(r'^node/create/subnodeof/(?P<father>\d+)/$', login_required(views.NodeCreate.as_view()), name='NodeCreate'),
	url(r'^node/(?P<pk>\d+)/edit/$', views.NodeUpdate.as_view(), name='NodeUpdate'),
#	url(r'^node/(?P<pk>\d+)/delete/$', views.NodeDelete.as_view(), name='NodeDelete'),
#	url(r'^link/(?P<pk>\d+)/edit/$', views.LinkUpdate.as_view(), name='LinkUpdate'),
#	url(r'^link/create/$', views.LinkCreate.as_view(), name='LinkCreate'),
#	
)

