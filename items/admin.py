from django.contrib import admin

from items.models import CacheItems, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(CacheItems)