from django.db import models

# Create your models here.
class data_analyst_register(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(null=True,unique=True)
    Phone_number = models.PositiveBigIntegerField(null=True,unique=True)
    Password = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)

class data_analyst_data(models.Model):
    Name_user = models.CharField(max_length=50)
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
    analyse = models.BooleanField(default=False)
    output = models.CharField(max_length=200,null=True)
    admin = models.BooleanField(default=False)



