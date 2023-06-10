from django.db import models

# Create your models here.
class emission_check(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(null=True,unique=True)
    Phone_number = models.PositiveBigIntegerField(null=True,unique=True)
    Password = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)


class emission_calculate(models.Model):
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
    send_to_analyse = models.BooleanField(default=False)



class userdatail(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date = models.IntegerField(null=True)
    no_of_peple = models.IntegerField(null=True)
    type_of_shelter = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
