from django import forms
from .models import WorkOrder


class OpenWorkForms(forms.ModelForm):

    class Meta:
        model = WorkOrder
        fields = ['request_description']

        widgets = {
            'request_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
            }),
        }

    def clean(self):
        return self.cleaned_data


class WorkForms(forms.ModelForm):

    class Meta:
        model = WorkOrder
        fields = ['job_description']

        widgets = {
            'job_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
            }),
        }

    def clean(self):
        return self.cleaned_data
