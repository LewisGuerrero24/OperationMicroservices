from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=250, null=True)
    nit = models.CharField(max_length=40, unique=True)
    country = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20, null=True)
    website = models.CharField(max_length=100, null=True)
    contact_name = models.CharField(max_length=100, null=True)
    contact_phone = models.CharField(max_length=20, null=True)
    contact_email = models.CharField(max_length=200, null=True)
    notes = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Company'


