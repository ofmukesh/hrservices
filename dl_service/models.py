from django.db import models
from utils.choices import StateChoices, StatusChoices
from utils.common import generate_uuid_with_prefix


class Dlfind(models.Model):
    id = models.CharField(
        max_length=255, default=generate_uuid_with_prefix('FINDDL'), primary_key=True, editable=False)
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    father_name = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(
        max_length=255, choices=StateChoices, blank=False, null=False)
    date_of_birth = models.DateField()
    dl_no = models.CharField(max_length=16, blank=False, null=False)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Dlpdf(models.Model):
    id = models.CharField(
        max_length=255, default=generate_uuid_with_prefix('DLPDF'), primary_key=True, editable=False)
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    dl_no = models.CharField(max_length=16, blank=False, null=False)
    name_as_per_dl = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField()
    file = models.FileField(upload_to='dl_files')
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)