from django.conf.urls import patterns, include, url
'''
ajax_urlpatterns = patterns('apps.cms.attendees.ajax',
    url(r'^send/$', 'send', name='send_attendee'),
    url(r'^export/$', 'export', name='export_attendee'),
)
urlpatterns = patterns('',
    url(r'^', include(views_urlpatterns)),
)
'''
urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index_homepage'),
)
