from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict

# Create your views here.
from jobmodel.models import Job


class Column:
    is_url = False,
    value = ""

    def __init__(self, value, is_url=False):
        self.value = value
        self.is_url = is_url


def display_job_details(request, job_id=""):
    if job_id == "":
        return HttpResponse("Error")

    company = Job.objects.filter(unique_url_id=job_id)
    if len(company) == 0:
        return HttpResponse("No Job listed with id = " + job_id)
    return render(request, 'job-details.html', model_to_dict(company[0]))


def show_all_jobs(request):
    jobs = Job.objects.all()
    jobs_arr = []
    for job in jobs:
        jobs_arr.append(model_to_dict(job))

    return render(request, 'job-listings.html', {
        "jobs": jobs_arr
    })
