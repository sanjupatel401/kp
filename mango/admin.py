from django.contrib import admin
from .models import product

# Register your models here.

class displaytable(admin.ModelAdmin):
    list_display=['name','price','details','link','brand_name','category','image']

admin.site.register(product,displaytable)