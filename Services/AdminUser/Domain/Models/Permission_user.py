from datetime import datetime
from typing import Optional
from Domain.Models import Permit
from Domain.Models.Permission_level import PermissionLevel
from Domain.Models.System_User import SystemUsers


class PermissionUser:
    def __init__(
        self, system_user: SystemUsers, permission_level: PermissionLevel,
        permit: Permit, status: bool = True,
        creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.system_user = system_user
        self.permission_level = permission_level
        self.permit = permit
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date