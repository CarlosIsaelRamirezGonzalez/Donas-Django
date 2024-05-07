from django.contrib import admin
from .models import Orden

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('datecompleted',)

admin.site.register(Orden, TaskAdmin)
