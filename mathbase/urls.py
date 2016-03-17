from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tree/', include('tree.urls', namespace='tree')),
	url(r'^$', RedirectView.as_view(url='tree/', permanent=False), name='index'),
)
