from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from tree import views

urlpatterns = patterns('',
	url(r'^$', views.ListNode.as_view(), name='ListNode'),
	url(r'^node/(?P<pk>\d+)/$', views.ShowNode.as_view(), name='ShowNode'),
	url(r'^node/create/subnodeof/(?P<father>\d+)/$', login_required(views.NodeCreate.as_view()), name='NodeCreate'),
	url(r'^node/(?P<pk>\d+)/edit/$', login_required(views.NodeUpdate.as_view()), name='NodeUpdate'),
	url(r'^node/(?P<pk>\d+)/delete/$', login_required(views.NodeDelete.as_view()), name='NodeDelete'),
	url(r'^link/(?P<pk>\d+)/edit/next/(?P<next>\d+)/$', login_required(views.LinkUpdate.as_view()), name='LinkUpdate'),
	url(r'^link/create/next/(?P<next>\d+)/$', login_required(views.LinkCreate.as_view()), name='LinkCreate'),
	url(r'^link/(?P<pk>\d+)/delete/next/(?P<next>\d+)/$', login_required(views.LinkDelete.as_view()), name='LinkDelete'),
	url(r'^tag/create/next/(?P<next>\d+)/$', login_required(views.TagCreate.as_view()), name='TagCreate'),
)

