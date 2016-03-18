from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tree/', include('tree.urls', namespace='tree')),
	url(r'^login/', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/tree'}, name='logout'),
	url(r'^$', RedirectView.as_view(url='tree/', permanent=False), name='index'),
)

admin.site.site_header = 'MATHBASE administration'
admin.site.site_title = 'MATHBASE admin page'
