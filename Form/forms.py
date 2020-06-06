from django import forms
from.models import *

class ReportingForm(forms.ModelForm):
    incident_description = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'cols': '80'}))
    incident_location = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols': '80'}))
    suspected_cause = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols': '80'}))
    immediate_action_taken = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'cols': '80'}))
    class Meta:
        model=Reporting
        fields="__all__"






