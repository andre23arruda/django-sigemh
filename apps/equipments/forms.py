from django import forms
from .models import Equipment
from work_order.models import WorkOrder


class SelectWorkForms(forms.ModelForm):
    # equipment = forms.CharField(
    #     disabled=True,
    #     widget=forms.TextInput(attrs={'class': 'form-control'})
    # )
    work_order = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Equipment
        # fields = ['equipment', 'work_order']
        fields = ['work_order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            # self.fields['equipment'].initial = instance
            self.fields['work_order'].queryset = instance.equipment_works.all()
            # self.fields['work_order'].queryset = instance.equipment_works.filter(status=1)

    def clean(self):
        return self.cleaned_data


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