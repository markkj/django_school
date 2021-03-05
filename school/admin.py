from django.contrib import admin
from .models import Student ,School

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['first_name','last_name','school']

class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ['name','address']


admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)