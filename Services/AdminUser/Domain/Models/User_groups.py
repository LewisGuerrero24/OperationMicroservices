from datetime import datetime
from typing import Optional
from Domain.Models.Groups import Groups
from Domain.Models.System_User import SystemUsers


class UserGroups:
    def __init__(
        self, system_user: SystemUsers, group: Groups,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.system_user = system_user
        self.group = group
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date