from datetime import datetime
from typing import Optional
from uuid import UUID
from Domain.Models import Spaces


class SystemUsers:
    def __init__(
        self, id: UUID, spaces: Spaces, full_name: str, username: str, email: str,
        password: str, is_superuser: bool = False, last_login: Optional[datetime] = None,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.id = id
        self.spaces = spaces
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password
        self.is_superuser = is_superuser
        self.last_login = last_login
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date