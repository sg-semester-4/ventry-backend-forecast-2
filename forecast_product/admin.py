from django.contrib import admin

from . import models

admin.site.register(models.Account)
admin.site.register(models.Item)
admin.site.register(models.ItemCombination)
admin.site.register(models.Product)
admin.site.register(models.ProductItem)
admin.site.register(models.InventoryControl)
admin.site.register(models.ProductTransaction)

# Register your models here.
