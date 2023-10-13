from django import forms
from django.conf import settings
from .models import *


class PanFindForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date of Birth (dd/mm/yyyy)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Panfind
        fields = ['aadhar_no', 'date_of_birth']

class InstantPanFindForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = InstantPanfind
        fields = ['aadhar_no']


class PanPdfForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date of Birth (dd/mm/yyyy)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Panpdf
        fields = ['pan_no', 'aadhar_no', 'date_of_birth']


class AadharToPanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Panpdf
        fields = ['aadhar_no']


class UtiPanPdfForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS, label='Date of Birth (dd/mm/yyyy)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Utipanpdf
        fields = ['full_name','father_name','pan_no', 'aadhar_no', 'date_of_birth','photo','sign']