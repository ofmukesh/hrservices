from django.db import models


class Service(models.Model):
    id = models.CharField(max_length=55, primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    charge = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
