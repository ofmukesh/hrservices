from django import forms
from .models import Voterpdf

class VoterPdfForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Voterpdf
        fields = ['epic_no', 'name_as_voter']
