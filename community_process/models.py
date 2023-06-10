from django.db import models

# Create your models here.
class community_process(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(null=True,unique=True)
    Phone_number = models.PositiveBigIntegerField(null=True,unique=True)
    Password = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)