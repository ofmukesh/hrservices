from django.db import models
from utils.choices import StatusChoices,GenderChoices


class Covid(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=15, blank=False, null=False)
    mobile_no = models.CharField(max_length=10, blank=False, null=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    gender = models.CharField(
        max_length=255, choices=GenderChoices, blank=False, null=False)
    date_of_birth=models.DateField()
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
