from django.db import models
from utils.choices import StatusChoices,VoterTypeChoices


class Voterpdf(models.Model):
    account = models.ForeignKey(
        'accounts.account', on_delete=models.CASCADE, editable=False)
    epic_no = models.CharField(max_length=15, blank=False, null=False)
    name_as_voter = models.CharField(max_length=255, blank=False, null=False)
    voter_type = models.CharField(
        max_length=255, choices=VoterTypeChoices, default=1, blank=False, null=False)
    file = models.FileField(upload_to='voter_files')
    status = models.CharField(choices=StatusChoices,
                              max_length=255, default='pending')
    tid=models.OneToOneField('accounts.transactions', on_delete=models.CASCADE,null=True,default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
