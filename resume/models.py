from django.db import models


class PersonalData(models.Model):
    Name = models.CharField(max_length=30)
    Address = models.TextField()
    City = models.CharField(max_length=20)
    Zipcode = models.IntegerField()
    Country = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone = models.IntegerField()


class Files(models.Model):
    Excel = models.FileField(upload_to='excel/')
    Html = models.FileField(upload_to='templates/')
    Subject = models.CharField(default='Sample', max_length=200)
