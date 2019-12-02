from django.contrib import admin
from .models import Employees
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


class DisplayEmployee(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'gender', 'birth_date', 'hire_date')
    search_fields = ['first_name']
    list_filter = ('gender', ('birth_date', DateRangeFilter))

    ordering = ('last_name', 'hire_date')


admin.site.register(Employees, DisplayEmployee)
