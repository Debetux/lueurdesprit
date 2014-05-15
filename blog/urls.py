from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^articles/(?P<category>.+)$', views.view_entry_in_category, name="view_entry_in_category"),
    url(r'article/(?P<slug>.+)', views.view_entry, name='view_entry')
)