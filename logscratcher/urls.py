from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logscratcher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'scratcher.views.home', name='home'),
    url(r'^refresh_log_data/(\d+)/$', 'scratcher.views.refresh_log_data', name='refresh_log_data'),
)
