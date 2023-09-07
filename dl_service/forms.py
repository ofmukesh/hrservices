from django import forms
from django.conf import settings
from .models import Dlfind, Dlpdf


class DlFindForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date of Birth (dd/mm/yyyy)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Dlfind
        fields = ['name', 'father_name', 'state', 'date_of_birth']


class DlPdfForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date of Birth (dd/mm/yyyy)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Dlpdf
        fields = ['dl_no', 'name_as_per_dl', 'date_of_birth']
