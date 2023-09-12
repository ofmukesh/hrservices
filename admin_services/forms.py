from django import forms


class VoterRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # adding css class to form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    photo = forms.ImageField(label='Photo', required=False)
    voter_no = forms.CharField(label='Voter Number', max_length=16)
    elector_name = forms.CharField(label='Elector Name', max_length=100)
    father_mother_husband_name = forms.CharField(
        label='Father/Mother/Husband Name', max_length=100)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    sex = forms.ChoiceField(
        label='Sex', choices=SEX_CHOICES)
    age = forms.IntegerField(label='Age')
    address1 = forms.CharField(label='Address Line 1', max_length=200)
    address2 = forms.CharField(
        label='Address Line 2', max_length=200, required=True)
    place = forms.CharField(label='Place', max_length=100)
    date = forms.DateField(label='Date of Registration ', widget=forms.TextInput(attrs={'type': 'date'}))
