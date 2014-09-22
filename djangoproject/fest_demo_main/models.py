from django.db import models

# Create your models here.


class Medication(models.Model):
    name = models.TextField(unique=True)
    atc_code = models.TextField()
