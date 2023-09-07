from django import forms
from django.conf import settings
from .models import Aadharfind, Aadharpdf


class AadharFindForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date (dd/mm/yyyy)')
    time = forms.TimeField(
        input_formats=settings.TIME_INPUT_FORMATS, label='Time (Hours:Minutes:Seconds)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Aadharfind
        fields = ['name', 'enrollment_no', 'time', 'date']


class AadharPdfForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date (dd/mm/yyyy)')
    time = forms.TimeField(
        input_formats=settings.TIME_INPUT_FORMATS, label='Time (Hours:Minutes:Seconds)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Aadharpdf
        fields = ['name', 'enrollment_no', 'time', 'date']
