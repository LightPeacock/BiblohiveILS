from django.db import models

# Create your models here.

class Book(models.Model):
    bid = models.BigIntegerField()
    btitle = models.CharField(max_length=128)
    author = models.CharField(max_length=150)
    bcopies = models.BigIntegerField()

