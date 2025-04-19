from datetime import datetime
from typing import Optional

class LicenseType:
    def __init__(
        self, name: Optional[str], description: Optional[str], price: float,
        support_level: str, duration_days: int, max_users: int,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.name = name
        self.description = description
        self.price = price
        self.support_level = support_level
        self.duration_days = duration_days
        self.max_users = max_users
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date