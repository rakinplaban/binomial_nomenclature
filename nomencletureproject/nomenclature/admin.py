from django.contrib import admin
from .models import ScientificName, Contact

class Sci_name(admin.ModelAdmin):
    list_display = ("id","sci_name","real_name")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

admin.site.register(ScientificName,Sci_name)

# admin.site.register()
# Register your models here.
