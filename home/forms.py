from django import forms
from .models import Report, Summary

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ( 'name','maxAmount')


class SummaryForm(forms.ModelForm):

    class Meta:
        model = Summary
        fields = ( 'summary',)

