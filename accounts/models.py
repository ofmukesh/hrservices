from django.db import models
from utils.common import generate_uuid_10


# Create your models here.
class Account(models.Model):
    id = models.CharField(
        max_length=10, default=generate_uuid_10(), primary_key=True, editable=False)
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, null=False, blank=False)
    contact_no = models.CharField(max_length=10, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
