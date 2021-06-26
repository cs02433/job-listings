from django.contrib import admin
from jobmodel.models import Job

# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "url")

