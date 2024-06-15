from django.contrib import admin
from rangefilter.filters import NumericRangeFilterBuilder
from .models import Donut


@admin.register(Donut)
class DonutAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'description', 'nutritional_information']
    list_filter = (
        ('quantity', NumericRangeFilterBuilder()),
        ('price', NumericRangeFilterBuilder()),
    )
    search_fields = ['name', 'description']
    ordering = ['name']


