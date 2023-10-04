from django.db import models

class VoterRegistration(models.Model):
    photo = models.ImageField(blank=False,upload_to='voter_photos')
    address1 = models.CharField(max_length=255)
    voter_no = models.CharField(max_length=16)

    def __str__(self):
        return self.voter_no
