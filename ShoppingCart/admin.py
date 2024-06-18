from django.contrib import admin
from rangefilter.filters import NumericRangeFilterBuilder
from django.utils import timezone

from .models import ShoppingCart, Order

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'donut', 'quantity', 'suggestion', 'bill', 'ordered']
    list_filter = (
        ('quantity', NumericRangeFilterBuilder()),
    )
    search_fields = ['user', 'donut']
    ordering = ['user']


from django.contrib import admin
from .models import Order

class DateArrivedFilter(admin.SimpleListFilter):
    title = 'Date Arrived'
    parameter_name = 'date_arrived'

    def lookups(self, request, model_admin):
        return (
            ('passed', 'Passed Date Arrived'),
            ('not_passed', 'Not Passed Date Arrived'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'passed':
            return queryset.filter(date_arrived__lt=timezone.now())
        elif self.value() == 'not_passed':
            return queryset.filter(date_arrived__gte=timezone.now())
        else:
            return queryset

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['address', 'quantity', 'status', 'user', 'donut', 'date_arrived']
    list_filter = ('status', DateArrivedFilter)  # Agrega el filtro personalizado
    search_fields = ['address', 'user__username', 'donut__name']  # Modifica la búsqueda para user y donut
    ordering = ['user']
