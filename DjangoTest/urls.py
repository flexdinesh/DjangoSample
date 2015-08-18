from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'test_app.views.home', name='home'),
    url(r'^index/', 'test_app.views.index', name='index'),
    url(r'^test_app/', 'test_app.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)
