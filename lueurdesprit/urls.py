from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

from filebrowser.sites import site


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lueurdesprit.views.home', name='home'),
    url(r'^oeuvre/', include('work.urls', namespace='work')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
