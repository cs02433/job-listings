from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=500)
    state = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    qualification = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    hiring_process = models.CharField(max_length=500)
    is_goverment_job = models.BooleanField()
    unique_url_id = models.CharField(max_length=500, default="")
    general_application_fees = models.CharField(max_length=500, default="")
    sc_st_application_fees = models.CharField(max_length=500, default="")
    ph_application_fees = models.CharField(max_length=500, default="")
    how_to_pay_fees = models.CharField(max_length=500, default="")

    exam_date = models.CharField(max_length=100, default="")
    exam = models.CharField(max_length=500, default="")

    last_date_to_fee_payment = models.CharField(max_length=500, default="")
    start_date_to_apply = models.CharField(max_length=500, default="")
    eligibility = models.CharField(max_length=500, default="")
    end_date_to_apply = models.CharField(max_length=500, default="")
    minimum_age = models.CharField(max_length=500, default="")
    maximum_age = models.CharField(max_length=500, default="")
    age_relaxation = models.CharField(max_length=500, default="")
    how_to_apply = models.CharField(max_length=500)

    def __str__(self):
        return self.title
