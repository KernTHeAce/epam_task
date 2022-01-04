from django.contrib import admin

# Register your models here.
from .models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Department)
admin.site.register(Employee)

def trigger():
    empl_query = Employee.objects.filter()
    dep_query = Department.objects.filter()

    for department_item in dep_query:
        empl_num = Employee.objects.filter(department = str(department_item)).count()
        print(empl_num)
        
