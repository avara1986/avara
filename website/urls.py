from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
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
                       url(r'^projects/wema/$', TemplateView.as_view(
                           template_name='website/projects_wema.html')),
                       url(r'^projects/atenea/$', TemplateView.as_view(
                           template_name='website/projects_atenea.html')),
                       url(r'^projects/revengebook/$', TemplateView.as_view(
                           template_name='website/projects_revengebook.html')),
                       url(r'^projects/olif/$', TemplateView.as_view(
                           template_name='website/projects_olif.html')),
                       url(r'^projects/olimpo/$', TemplateView.as_view(
                           template_name='website/projects_olimpo.html')),
                       url(r'^thanks/$', TemplateView.as_view(
                           template_name='website/thanks.html')),
                       url(r'^cv/$', TemplateView.as_view(
                           template_name='website/cv.html')),
                       url(r'^8reinas/$', 'ochoReinas', name='ochoReinas'),
                       url(r'^contact/$', 'contact', name='contact'),
                       url(r'^$', 'index', name='index_homepage'),
                       )
