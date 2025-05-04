from typing import Optional, List
from datetime import datetime
from uuid import UUID

class Company:
    def __init__(
        self, name: str, legal_name: Optional[str], nit: str, country: str, location: str,
        phone: int, email: str, postal_code: Optional[str], website: Optional[str],
        contact_name: Optional[str], contact_phone: Optional[str], contact_email: Optional[str],
        notes: Optional[str], status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.name = name
        self.legal_name = legal_name
        self.nit = nit
        self.country = country
        self.location = location
        self.phone = phone
        self.email = email
        self.postal_code = postal_code
        self.website = website
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.notes = notes
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date