from django import forms
from .models import Covid
from django.conf import settings

class CovidForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date of Birth (dd/mm/yyyy)')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Covid
        fields = ['name', 'mobile_no','aadhar_no','date_of_birth','gender']
