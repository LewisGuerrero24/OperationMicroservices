from django.db import models

class UserModelBd(models.Model):
    name = models.CharField(max_length=100)
    edad = models.CharField(max_length=4)   
