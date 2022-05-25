
from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'completion_time')
    date_hierarchy = 'creation_time'

class TaskAdmin(admin.ModelAdmin):
     list_filter = ('project', 'completed')
     search_fields = ['title']


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task,TaskAdmin)
