from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/projects/')), 
    #url(r'^$', 'harvardd4d.views.home', name='home'),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^admin/', include(admin.site.urls)),
)
