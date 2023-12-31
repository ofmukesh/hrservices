from django.db import models
from utils.choices import StatusChoices


class Panfind(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    pan_no = models.CharField(max_length=255, default='', blank=True)
    date_of_birth = models.DateField()
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Panpdf(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    pan_no = models.CharField(max_length=10, blank=False, null=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    date_of_birth = models.DateField()
    file = models.FileField(upload_to='pan_pdfs',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class AadharToPan(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    pan_no = models.CharField(max_length=255, blank=False,null=False)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Allpanpdf(models.Model):
    photo = models.ImageField(blank=False,null=False,upload_to='pan_photos')
    sign = models.ImageField(blank=False,null=False,upload_to='pan_photos')
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    pan_no = models.CharField(max_length=10, blank=False, null=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    date_of_birth = models.DateField()
    file = models.FileField(upload_to='pan_pdfs',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class InstantPanfind(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    aadhar_no = models.CharField(max_length=12, blank=False, null=False)
    pan_no = models.CharField(max_length=255, default='', blank=True)
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)