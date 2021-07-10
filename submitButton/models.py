from django.db import models

# Create your models here.


class TestModel(models.Model):
    input1= models.CharField(max_length=200)
    input2 = models.CharField(max_length=200)