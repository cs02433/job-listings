from django import forms
from django.db import models


class JobSourceWebsite(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=500)


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default="")
    short_description = models.CharField(max_length=500)
    state = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    qualification = models.CharField(max_length=1000)
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
    end_date_to_apply = models.CharField(max_length=500, default="")
    eligibility = models.CharField(max_length=500, default="")
    minimum_age = models.CharField(max_length=500, default="")
    maximum_age = models.CharField(max_length=500, default="")
    age_relaxation = models.CharField(max_length=500, default="")
    how_to_apply = models.CharField(max_length=500)
    notification_url = models.CharField(max_length=500)
    application_form_url = models.CharField(max_length=500)
    logo_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    title = forms.CharField(widget=forms.TextInput(attrs={'size': 100}))
    company = forms.CharField(widget=forms.TextInput(attrs={'size': 100}))
    short_description = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    state = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))
    category = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))
    salary = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 50}))
    qualification = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    url = forms.URLField()
    hiring_process = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    is_goverment_job = forms.BooleanField()
    unique_url_id = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    general_application_fees = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    sc_st_application_fees = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    ph_application_fees = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    how_to_pay_fees = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    exam_date = forms.CharField(initial="")
    exam = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))

    last_date_to_fee_payment = forms.CharField()
    start_date_to_apply = forms.CharField()
    end_date_to_apply = forms.CharField()
    eligibility = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))
    minimum_age = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))
    maximum_age = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))
    age_relaxation = forms.CharField(initial="N/A", widget=forms.TextInput(attrs={'size': 100}))
    how_to_apply = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    notification_url = forms.URLField()
    application_form_url = forms.URLField()
    logo_url = forms.URLField()

    def __str__(self):
        return self.title
