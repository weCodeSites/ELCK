from django.db import models

# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phonenumber=models.IntegerField()
    county=models.TextField(default="")
    college=models.TextField(default="")
    def __str__(self):
        return self.firstname +"  "+self.lastname + "  "+ self.college + "  "+ self.phonenumber
    class Meta:
        verbose_name_plural="Members"
    

class WeeklyDevotion(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(default="")
    new=models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="WeeklyDevotion"

class Gallery(models.Model):
    image=models.ImageField(upload_to="media")
    title=models.CharField(max_length=50)
    description=models.TextField(default="")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Gallery"

class Events(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=60)
    decription=models.CharField(max_length=60)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Events"

