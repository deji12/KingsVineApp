from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.brand)
admin.site.register(models.clothing)
admin.site.register(models.shoe)
admin.site.register(models.face_and_body)
admin.site.register(models.accessories)
admin.site.register(models.beauty)
admin.site.register(models.kids)