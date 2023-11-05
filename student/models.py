from django.db import models

# Create your models here.

class student(models.Model):
    sname = models.CharField(max_length=128)
    sid = models.BigIntegerField()
    sphone = models.BigIntegerField()
    snumber =  models.BigIntegerField()
