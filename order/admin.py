from django.contrib import admin
from . models import *
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price',]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid', 'first_name', 'last_name', 'datetime_creat']
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price',]