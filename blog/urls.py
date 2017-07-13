from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
