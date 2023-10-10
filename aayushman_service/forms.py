from django import forms
from .models import AayushmanPdf

class AayushmanPdfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = AayushmanPdf
        fields = ('state', 'parameter_type', 'parameter_no')
