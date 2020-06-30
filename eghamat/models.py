from django.db import models


# Create your models here.
class Room(models.Model):
    Room_Zarfiat = models.IntegerField()
    Room_Price = models.IntegerField()
    Room_type = models.CharField(max_length=50)
    Room_Image = models.ImageField(upload_to='images/', null=True, blank=True)
    Room_About = models.TextField()


class User(models.Model):
    User_Fname = models.CharField(max_length=30)
    User_Lname = models.CharField(max_length=50)
    User_Mobile = models.CharField(max_length=11)
    User_Phone = models.IntegerField()
    User_Email = models.EmailField()
    User_Gender = models.CharField(max_length=10)
    User_BirthDay = models.DateField()


class Reservation(models.Model):
    Reserve_Date = models.DateField()
    Reserve_Dayes = models.SmallIntegerField()
