from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=200)
    codeService = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=False)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Services'