from datetime import datetime
from typing import Optional


class Services:
    def __init__(
        self, name: str, code_service: str, description: str,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.name = name
        self.code_service = code_service
        self.description = description
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date
