from django.db import models

# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phonenumber=models.IntegerField()
    county=models.TextField(default="")
    college=models.TextField(default="")

