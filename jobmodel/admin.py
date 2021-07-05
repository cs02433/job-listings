from django.contrib import admin
from jobmodel.models import Job, JobSourceWebsite, JobForm


# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    form = JobForm
    list_display = ("title", "short_description")


@admin.register(JobSourceWebsite)
class JobSourceWebsiteAdmin(admin.ModelAdmin):
    list_display = ("title", "url")
