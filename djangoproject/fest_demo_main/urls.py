from django.conf.urls import patterns, url

from fest_demo_main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)