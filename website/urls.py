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
                       url(r'^8reinas/$', 'ochoReinas', name='ocho_reinas'),
                       url(r'^dnscheck/$', 'dnscheck', name='dns_check'),
                       url(r'^contact/$', 'contact', name='contact'),
                       url(r'^cv/$', TemplateView.as_view(
                           template_name='website/cv.html'), name="cv"),
                       url(r'^projects/wema/$', TemplateView.as_view(
                           template_name='website/projects_wema.html'), name="project_wema"),
                       url(r'^projects/atenea/$', TemplateView.as_view(
                           template_name='website/projects_atenea.html'), name="project_atenea"),
                       url(r'^projects/cssbeautifier/$', TemplateView.as_view(
                           template_name='website/projects_cssbeautifier.html'), name="project_cssbeautifier"),
                       url(r'^projects/revengebook/$', TemplateView.as_view(
                           template_name='website/projects_revengebook.html'), name="project_rb"),
                       url(r'^projects/olif/$', TemplateView.as_view(
                           template_name='website/projects_olif.html'), name="project_olif"),
                       url(r'^projects/olimpo/$', TemplateView.as_view(
                           template_name='website/projects_olimpo.html'), name="project_olimpo"),
                       url(r'^resources/$', 'resources', name='resources'),
                       url(r'^thanks/$', TemplateView.as_view(
                           template_name='website/thanks.html')),
                       url(r'^$', 'index', name='index_homepage'),
                       )
