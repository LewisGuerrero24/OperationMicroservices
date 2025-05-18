from datetime import datetime
from typing import Optional
from Domain.Models.Permit import  Permit
from Domain.Models.Groups import Groups
from Domain.Models.Permission_level import PermissionLevel


class PermissionGroup:
    def __init__(
        self, group: Groups, permission_level: PermissionLevel,
        permit: Permit, status: bool = True,
        creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.group = group
        self.permission_level = permission_level
        self.permit = permit
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date