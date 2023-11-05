from django.db import models

# Create your models here.

class faculty(models.Model):
    fid = models.BigIntegerField()
    fname = models.CharField()
    fphone = models.BigIntegerField()
    fnumber = models.BigIntegerField(max_length=2) # To get value of how many books are issued till now

class flogin(models.Model):
    username = models.CharField()
    firstname = models.CharField()
    lastname = models.CharField()
    password = models.CharField()
    email = models.EmailField()
    class meta:
        db_table = 'BiblohiveILS'
        using = 'flogin'

