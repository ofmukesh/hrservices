from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

        # Set min and max length for the username field
        self.fields['username'].widget.attrs['placeholder'] = "Enter your mobile no."
        self.fields['username'].widget.attrs['minlength'] = 10
        self.fields['username'].widget.attrs['maxlength'] = 10

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        labels = {
            "username": "Mobile no."
        }
