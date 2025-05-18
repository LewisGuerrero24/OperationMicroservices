from django.db import models
from .Spaces import Spaces

class Groups(models.Model):
    spaces = models.ForeignKey(Spaces, on_delete=models.PROTECT)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Groups'