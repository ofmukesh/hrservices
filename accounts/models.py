from django.db import models


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, null=False, blank=False)
    contact_no = models.CharField(max_length=10, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.contact_no)+f"( {self.user.first_name} {self.user.last_name} )"
    

class Transactions(models.Model):
    charged=models.IntegerField()
    balance=models.IntegerField()
    ac = models.ForeignKey('accounts.account', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ac.contact_no
    

class Addmoneytransactions(models.Model):
    money_added=models.IntegerField()
    balance=models.IntegerField()
    ac = models.ForeignKey('accounts.account', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.ac.contact_no