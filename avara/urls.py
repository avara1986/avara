from django.conf.urls import patterns, include, url
from django.contrib import admin
from avara import settings
from avara.routers import router
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^_ah/', include('djangae.urls')),
                       url(r'^api/v1/', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('website.urls')),
                       )

urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT}),
                        )
