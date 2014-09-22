from tastypie import authorization, resources

from fest_demo_main import models


class MedicationResource(resources.ModelResource):
    class Meta:
        queryset = models.Medication.objects.all()
        #authorization = authorization.Authorization()


