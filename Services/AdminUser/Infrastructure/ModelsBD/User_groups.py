from django.db import models
from .Groups import Groups
from .System_users import System_users

class User_groups(models.Model):
    system_user = models.ForeignKey(System_users, on_delete=models.PROTECT)
    group = models.ForeignKey(Groups, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'User_groups'