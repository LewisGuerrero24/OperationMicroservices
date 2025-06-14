from datetime import datetime
from typing import Optional
from Domain.Models.Services import Services
from Domain.Models.License_type import LicenseType


class LicenseTypeServices:
    def __init__(
        self, license_type: LicenseType, service: Services,
        max_records: int, duration_days: int, custom_limit_note: Optional[str],
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.license_type = license_type
        self.service = service
        self.max_records = max_records
        self.duration_days = duration_days
        self.custom_limit_note = custom_limit_note
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date