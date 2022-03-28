import code
from unicodedata import name
from django.db import models

class Product(models.Model):

    code = models.IntegerField()
    name = models.CharField(max_length=200)

    