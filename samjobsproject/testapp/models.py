from django.db import models

# Create your models here.
class hydjobs(models.Model):
    interviewdate=models.DateField()
    companyname=models.CharField(max_length=30)
    tittle=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    email=models.EmailField()
    phno=models.BigIntegerField()
class punejobs(models.Model):
    interviewdate=models.DateField()
    companyname=models.CharField(max_length=30)
    tittle=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    email=models.EmailField()
    phno=models.BigIntegerField()

class bangulorjobs(models.Model):
    interviewdate=models.DateField()
    companyname=models.CharField(max_length=30)
    tittle=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    email=models.EmailField()
    phno=models.BigIntegerField()
