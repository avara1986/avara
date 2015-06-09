from django.conf.urls import patterns, include, url
from avara import settings
from avara.api import QueueSendMail, SendToQueue, SendEmail
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'scaffold.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^_ah/', include('djangae.urls')),

                       # Note that by default this is also locked down with login:admin in
                       # app.yaml
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/send-queue/$', SendToQueue.as_view(),
                           name='queue-send-mail'),
                       url(r'^api/send-mail/$', SendEmail.as_view(),
                           name='send-mail'),
                       url(r'^api/queue/send-mail/$', QueueSendMail.as_view(),
                           name='queue-send-mail'),
                       url(r'^', include('website.urls')),
                       )

urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),
                        )
