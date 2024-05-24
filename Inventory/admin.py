from django.contrib import admin
from rangefilter.filters import NumericRangeFilter
from .models import Donut

@admin.register(Donut)
class DonutAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'description']
    list_filter = (
        ('quantity', NumericRangeFilter),
        ('price', NumericRangeFilter),
    )
    search_fields = ['name', 'description']
    ordering = ['price']


