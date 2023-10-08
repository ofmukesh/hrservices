from django.db import models

class VoterRegistration(models.Model):
    photo = models.ImageField(blank=False,upload_to='voter_photos')
    address1 = models.CharField(max_length=255)
    voter_no = models.CharField(max_length=16)

    def __str__(self):
        return self.voter_no

class VoterRegistrationOld(models.Model):
    photo = models.ImageField(blank=True,upload_to='voter_photos')
    voter_no = models.CharField(max_length=16)
    elector_name = models.CharField(max_length=100)
    father_mother_husband_name = models.CharField(max_length=100)
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    age = models.IntegerField()
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    date_of_registration = models.DateField()

    def __str__(self):
        return self.voter_no