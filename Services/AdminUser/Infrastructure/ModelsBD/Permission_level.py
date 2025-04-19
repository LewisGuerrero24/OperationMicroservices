from django.db import models

class Permission_level(models.Model):
    name = models.CharField(max_length=200, unique=True)
    level = models.PositiveIntegerField()
    description = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Permission_level'