from django.db import models as django_models
from django.conf import urls
from tastypie import exceptions, resources, utils
from tastypie_swagger import mapping

from fest_demo_main import models


class MedicationResource(resources.ModelResource):
    class Meta:
        queryset = models.Medication.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']

        extra_actions = [{
            'name': 'search',
            'summary': 'Search endpoint',
            'http_method': 'GET',
            'resource_type': 'list',
            'description': 'Search endpoint',
            'fields': {
                'query': {
                    'type': 'string',
                    'required': True,
                    'description': 'Search query terms'
                }
            }
        }]

    def prepend_urls(self):
        return [
            urls.url(
                r'^(?P<resource_name>%s)/search%s$' % (self._meta.resource_name, utils.trailing_slash()),
                self.wrap_view('get_search'), name='api_get_search'),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        query = request.GET.get('query', '')
        page = int(request.GET.get('page', 1))

        medications = models.Medication.objects.filter(
            django_models.Q(name__icontains=query) | django_models.Q(atc_code__icontains=query))[
                (page - 1) * 20:page * 20]

        objects = []
        for medication in medications:
            bundle = self.build_bundle(obj=medication, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)
