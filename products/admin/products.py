from django.contrib import admin
from products.models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = PRODUCT_DISPLAY