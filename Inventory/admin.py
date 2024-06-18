from django.contrib import admin
from rangefilter.filters import NumericRangeFilterBuilder
from datetime import datetime
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay
from .models import Donut, Profits


@admin.register(Donut)
class DonutAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'description', 'nutritional_information', 'date_expirity']
    list_filter = (
        ('quantity', NumericRangeFilterBuilder()),
        ('price', NumericRangeFilterBuilder()),
    )
    search_fields = ['name', 'description']
    ordering = ['name']



@admin.register(Profits)
class ProfitsAdmin(admin.ModelAdmin):
    list_display = ['profit', 'user', 'date_created']
    list_filter = ('user', 'date_created')
    search_fields = ['user__username']
    ordering = ['user']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            year=ExtractYear('date_created'),
            month=ExtractMonth('date_created'),
            day=ExtractDay('date_created'),
        )
        return queryset

    def changelist_view(self, request, extra_context=None):
        if 'date_created__year__exact' not in request.GET:
            q = request.GET.copy()
            q['date_created__year__exact'] = str(datetime.today().year)
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()
        return super().changelist_view(request, extra_context=extra_context)