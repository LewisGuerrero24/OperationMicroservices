from django.db import models

class User_Kafka(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
