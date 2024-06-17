from django.contrib import admin
from rangefilter.filters import NumericRangeFilterBuilder
from .models import ShoppingCart, Order

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'donut', 'quantity', 'suggestion', 'bill', 'ordered']
    list_filter = (
        ('quantity', NumericRangeFilterBuilder()),
    )
    search_fields = ['user', 'donut']
    ordering = ['user']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['address', 'quantity', 'status', 'user', 'donut']
    list_filter = ('status',)
    search_fields = ['address', 'user', 'donut']
    ordering = ['user']
