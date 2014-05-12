from django.conf.urls import patterns, url

from work import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^critique/(?P<type_of_work>.+)/(?P<slug>.+)/$', views.review_detail, name='review_detail'),
    url(r'^oeuvre/(?P<type_of_work>.+)/(?P<slug>.+)$', views.work_detail, name='work_detail'),

)