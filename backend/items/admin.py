from django.contrib import admin

from .models import Items

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ["id", "item_name", "item_category", "item_name"]


admin.site.register(Items,AdminProduct)