from django.contrib import admin

from .models import Cart

# Register your models here.
class AddtoCartAdmin(admin.ModelAdmin):
    list_display = ["id", "item_name", "user"]


admin.site.register(Cart,AddtoCartAdmin)