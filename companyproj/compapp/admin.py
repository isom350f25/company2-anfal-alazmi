from django.contrib import admin
from django.db import models
from .models import Employee, Project

# Register your models here.
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'amount')
    search_fields = ('name',)   
    list_filter = ('start_date', 'end_date')  
    inlines = [ProjectInline]
class Position(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


  

