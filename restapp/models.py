from django.db import models

# Create your models here.

# class Location(models.Model):
#     locationName=models.CharField(max_length=50)
#
# class ItemName(models.Model):
#     itemname=models.CharField(max_length=30)
#     dateAdded=models.DateField(auto_now_add=True)
#     location=models.ForeignKey(Location,on_delete=models.CASCADE)

class RegisterModel(models.Model):
    username=models.CharField(max_length=60,null=True)
    email=models.EmailField(null=True)
    phno=models.IntegerField(null=True)
    password=models.CharField(max_length=60,null=True)
    confirm=models.CharField(max_length=60,null=True)

    def __str__(self):
        return self.username

class Otp(models.Model):
    user=models.OneToOneField(RegisterModel,on_delete=models.CASCADE)
    otp=models.IntegerField(null=True)
