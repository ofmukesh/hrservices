from django import forms
from .models import VoterRegistration


class VoterRegistrationForm(forms.ModelForm):
    class Meta:
        model = VoterRegistration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding CSS classes and placeholders to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class SearchUserForm(forms.Form):
    mobile_no = forms.CharField(label="", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mobile_field = self.fields['mobile_no']
        mobile_field.widget.attrs['class'] = 'form-control'
        mobile_field.widget.attrs['placeholder'] = "Enter user mobile no."
        mobile_field.widget.attrs['maxlength'] = 10
        mobile_field.widget.attrs['minlength'] = 10

class AddMoneyForm(forms.Form):
    amount = forms.IntegerField(label="", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mobile_field = self.fields['amount']
        mobile_field.widget.attrs['class'] = 'form-control'
        mobile_field.widget.attrs['placeholder'] = "Enter amount"
        mobile_field.widget.attrs['maxlength'] = 10
        mobile_field.widget.attrs['minlength'] = 10