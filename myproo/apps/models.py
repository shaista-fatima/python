from django.db import models


# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    details=models.CharField(max_length=100)

def __str__(self):
    return self.title

