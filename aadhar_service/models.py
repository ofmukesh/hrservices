from django.db import models
from utils.choices import StatusChoices


class Aadharfind(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    enrollment_no = models.CharField(max_length=14, blank=False, null=False)
    time = models.TimeField()
    date = models.DateField()
    aadhar_no = models.CharField(max_length=16, blank=False, null=False)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Aadharpdf(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    enrollment_no = models.CharField(max_length=14, blank=False, null=False)
    time = models.TimeField()
    date = models.DateField()
    file = models.FileField(upload_to='aadhar_files',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Aadhaartopdf(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    aadhaar_no = models.CharField(max_length=12, blank=False, null=False)
    date_of_birth = models.DateField()
    file = models.FileField(upload_to='aadhar_files',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)