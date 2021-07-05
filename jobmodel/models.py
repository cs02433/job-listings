from django import forms
from django.db import models


class JobSourceWebsite(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=500)


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default="")
    short_description = models.CharField(max_length=500)
    qualification = models.CharField(max_length=1000)

    unique_url_id = models.CharField(max_length=500, default="")
    application_fees = models.CharField(max_length=1000, default="N/A")

    eligibility = models.CharField(max_length=1000, default="")

    start_date_to_apply = models.CharField(max_length=500, default="")
    end_date_to_apply = models.CharField(max_length=500, default="")

    last_date_to_fee_payment = models.CharField(max_length=500, default="")
    exam_date = models.CharField(max_length=100, default="")

    age = models.CharField(max_length=1000, default="N/A")
    age_relaxation = models.CharField(max_length=1000, default="")

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
    qualification = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    unique_url_id = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    application_fees = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    eligibility = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    exam_date = forms.CharField(initial="")

    last_date_to_fee_payment = forms.CharField()
    start_date_to_apply = forms.CharField()
    end_date_to_apply = forms.CharField()
    age = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    age_relaxation = forms.CharField(initial="N/A", widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    notification_url = forms.URLField()
    application_form_url = forms.URLField()
    logo_url = forms.URLField()

    def __str__(self):
        return self.title
