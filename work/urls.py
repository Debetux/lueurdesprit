from django.conf.urls import patterns, url

from work import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # List :
    url(r'^(?P<type_of_work>.+)/fiches/list/$', views.work_list, name="work_list"),
    url(r'^(?P<type_of_work>.+)/critiques/list/$', views.staffreview_list, name="staffreview_list"),

    # Details :
    url(r'^fiche/(?P<type_of_work>.+)/(?P<slug>.+)$', views.work_detail, name='work_detail'),
    url(r'^critique/(?P<type_of_work>.+)/(?P<work_slug>.+)/(?P<staffreview_id>\d+)$', views.review_detail, name='review_detail'),

)