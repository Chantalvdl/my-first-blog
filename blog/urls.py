from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^t/$', views.post_list_title, name='post_list_title'),
    url(r'^others/$', views.post_list_others, name='post_list_others'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^posts/', views.Postlist.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
