from django.db import models
from utils.choices import StateChoices, StatusChoices,OtherStateChoices


class Dlfind(models.Model):
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
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Dlpdf(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    dl_no = models.CharField(max_length=16, blank=False, null=False)
    name_as_per_dl = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField()
    file = models.FileField(upload_to='dl_files',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class OtherDlpdf(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    dl_no = models.CharField(max_length=16, blank=False, null=False)
    date_of_birth = models.DateField()
    state = models.CharField(max_length=50, choices=OtherStateChoices)
    file = models.FileField(upload_to='dl_files',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)