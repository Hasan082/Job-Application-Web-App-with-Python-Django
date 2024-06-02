from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date', 'ocupation')

admin.site.register(Job, JobAdmin)
