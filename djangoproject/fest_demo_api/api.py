from django.db import models as django_models
from tastypie import exceptions, resources

from fest_demo_main import models


class MedicationResource(resources.ModelResource):
    class Meta:
        queryset = models.Medication.objects.all()


class MedicationSearchResource(resources.ModelResource):
    class Meta:
        queryset = models.Medication.objects.all()
        resource_name = 'search'

    def get_object_list(self, request, **kwargs):
        query = request.GET.get('query', None)
        if not query:
            raise exceptions.BadRequest('Missing query parameter')

        return super(MedicationSearchResource, self).get_object_list(request).filter(
            django_models.Q(name__icontains=query) | django_models.Q(atc_code__icontains=query))

