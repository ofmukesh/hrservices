from django import forms
from .models import VoterRegistration


class VoterRegistrationForm(forms.ModelForm):
    date_of_registration = forms.DateField(label='Date of Registration ',
                           widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = VoterRegistration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding CSS classes and placeholders to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
