from django.db import models
from utils.choices import StateChoices,StatusChoices

class AayushmanPdf(models.Model):
    PARAMETER_TYPE_CHOICES = (
        ('AE-PMIAY ID', 'AE-PMIAY ID'),
        ('Family-ID/SAMAGRA D/NFSA Ration Card Number/HHID', 'Family-ID/SAMAGRA D/NFSA Ration Card Number/HHID'),
        ('Mobile Number', 'Mobile Number'),
    )

    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    state = models.CharField(max_length=50, choices=StateChoices)
    parameter_type = models.CharField(max_length=100, choices=PARAMETER_TYPE_CHOICES)
    parameter_no = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to='aayushman_files',blank=True,null=True)
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None,blank=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)