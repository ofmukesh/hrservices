from django.db import models
from utils.choices import StatusChoices
from utils.common import generate_uuid_with_prefix


class Nsdlpanfind(models.Model):
    id = models.CharField(
        max_length=255, default=generate_uuid_with_prefix('FINDPAN'), primary_key=True, editable=False)
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    name_as_pan = models.CharField(max_length=255, blank=False, null=False)
    pan_no = models.CharField(max_length=255, default='', blank=True)
    date_of_birth = models.DateField()
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Panpdf(models.Model):
    id = models.CharField(
        max_length=255, default=generate_uuid_with_prefix('PDFPAN'), primary_key=True, editable=False)
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    pan_no = models.CharField(max_length=10, blank=False, null=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    date_of_birth = models.DateField()
    file = models.FileField(upload_to='pan_pdfs')
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
