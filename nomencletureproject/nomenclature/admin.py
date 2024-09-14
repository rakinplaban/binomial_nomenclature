from django.contrib import admin
from .models import ScientificName

class Sci_name(admin.ModelAdmin):
    list_display = ("id","sci_name","real_name")

admin.site.register(ScientificName,Sci_name)
# admin.site.register()
# Register your models here.
