from datetime import datetime
from typing import Optional
from Domain.Models import Company

class Spaces:
    def __init__(
        self, company: int, code: str, name: str, description: str,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.company = company
        self.code = code
        self.name = name
        self.description = description
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date