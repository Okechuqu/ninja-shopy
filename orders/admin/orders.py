from django.contrib import admin
from orders.models import *
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ORDER_DISPLAY


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ORDER_ITEM_DISPLAY
