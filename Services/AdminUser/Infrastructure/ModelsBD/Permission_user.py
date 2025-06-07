from django.db import models
from .System_users import System_users
from .Permission_level import Permission_level
from .Permit import Permit
from django.utils import timezone

class Permission_user(models.Model):
    system_user = models.ForeignKey(System_users, on_delete=models.PROTECT)
    permission_level = models.ForeignKey(Permission_level, on_delete=models.PROTECT)
    permit = models.ForeignKey(Permit, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Permission_user'