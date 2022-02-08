from django.db import models

class Account(models.Model):
    address = models.CharField(max_length=100, null=False, blank=False)
    balance = models.BigIntegerField()

    def __str__(self):
        return f'{self.address} - {self.balance}'

    def delete_everything(self):
        Account.objects.all().delete()
