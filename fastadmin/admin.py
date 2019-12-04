from django.contrib import admin
from .models import Employees, Departments, Cat
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.utils.safestring import mark_safe


class DisplayEmployee(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'gender', 'birth_date', 'hire_date')
    search_fields = ['first_name']
    list_filter = ('gender', ('birth_date', DateRangeFilter))
    readonly_fields = ['emp_no', 'birth_date', 'gender']

    ordering = ('last_name', 'hire_date')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class DisplayCat(admin.ModelAdmin):
    fields = ('name', 'age', 'photo')
    list_display = ('name', 'age', 'photo', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width={obj.photo.width} height={obj.photo.height} />')


admin.site.register(Employees, DisplayEmployee)
admin.site.register(Cat, DisplayCat)
admin.site.register(Departments)
