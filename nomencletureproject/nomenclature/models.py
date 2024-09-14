from django.db import models

# Create your models here.
class ScientificName(models.Model):
    sci_name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)

    