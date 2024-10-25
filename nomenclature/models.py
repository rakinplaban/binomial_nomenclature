from django.db import models

# Create your models here.
class ScientificName(models.Model):
    sci_name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sci_name
    



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
