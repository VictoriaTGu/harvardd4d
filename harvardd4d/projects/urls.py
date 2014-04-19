from django.conf.urls import patterns, include, url
import projects.views

urlpatterns = patterns('',
    url(r'^$', projects.views.index, name='index'),
    url(r'^about/$', projects.views.about, name='about'),
    url(r'^titw/$', projects.views.titw, name='titw'),
    url(r'^idhack/$', projects.views.idhack, name='idhack'),
    url(r'^ttp/$', projects.views.ttp, name='ttp'),
    url(r'^discuss/$', projects.views.discuss, name='discuss'),
    url(r'^events/$', projects.views.events, name='events'),
    url(r'^external/$', projects.views.external, name='external'),
    url(r'^partners/$', projects.views.partners, name='partners'),
    url(r'^sponsors/$', projects.views.sponsors, name='sponsors'),
    url(r'^past_sponsors/$', projects.views.past_sponsors, name='past_sponsors'),
    url(r'^contact_us/$', projects.views.contact_us, name='contact_us'),
    #url(r'^partners/$', projects.views.partners, name='partners'),
)
