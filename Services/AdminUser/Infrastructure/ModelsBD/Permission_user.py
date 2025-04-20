from django.db import models
from .System_users import System_users
from .Permission_level import Permission_level
from .Permit import Permit

class Permission_user(models.Model):
    system_user = models.ForeignKey(System_users, on_delete=models.PROTECT)
    permission_level = models.ForeignKey(Permission_level, on_delete=models.PROTECT)
    permit = models.ForeignKey(Permit, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)