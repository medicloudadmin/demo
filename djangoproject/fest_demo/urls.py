from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie import api

from fest_demo_api import api as fest_demo_api

admin.autodiscover()

v1_api = api.Api(api_name='v1')
v1_api.register(fest_demo_api.MedicationResource())


urlpatterns = patterns(
    '',
    url(r'^$', include('fest_demo_main.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
