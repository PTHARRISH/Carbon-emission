from django.db import models

# Create your models here.
class admin_calcu(models.Model):
    petrol = models.IntegerField(null=True)
    diesel = models.IntegerField(null=True)
    gas = models.IntegerField(null=True)
    taxi = models.IntegerField(null=True)
    localbus = models.IntegerField(null=True)
    train = models.IntegerField(null=True)
    lpg_cyclinder = models.IntegerField(null=True)
    electricity = models.IntegerField(null=True)
    Total_emission = models.IntegerField(null=True)
    emission_calculate = models.BooleanField(default=False)