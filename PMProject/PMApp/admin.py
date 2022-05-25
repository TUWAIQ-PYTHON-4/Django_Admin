
from django.contrib import admin
from .models import Project,Task

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'creation_time')
  date_hierarchy = 'creation_time'




class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','time_estimation')
    list_filter = ('title',)
    search_fields = ['title']





