from datetime import datetime
from typing import Optional


class Module:
    def __init__(
        self, name: str, description: Optional[str] = None,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.name = name
        self.description = description
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date