from django.conf.urls import patterns, url

from work import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<type_of_work>.+)/$', views.work_list, name="work_list"),
    url(r'^(?P<type_of_work>.+)/critiques/$', views.staffreview_list, name="staffreview_list"),
    url(r'^critique/(?P<type_of_work>.+)/(?P<slug>.+)/$', views.review_detail, name='review_detail'),
    url(r'^fiche/(?P<type_of_work>.+)/(?P<slug>.+)$', views.work_detail, name='work_detail'),

)