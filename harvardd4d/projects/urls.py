from django.conf.urls import patterns, include, url
import projects.views

urlpatterns = patterns('',
    url(r'^$', projects.views.index, name='index'),
)
