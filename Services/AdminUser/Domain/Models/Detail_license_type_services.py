from datetime import datetime
from typing import Optional
from Domain.Models.Company_license_detail import CompanyLicenseDetail
from Domain.Models.License_type_services import LicenseTypeServices


class DetailLicenseTypeServices:
    def __init__(
        self, license_type_services: LicenseTypeServices,
        company_license_detail: CompanyLicenseDetail,
        allowed_limit: int, used_limit: int = 0, unit: str = 'registros',
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.license_type_services = license_type_services
        self.company_license_detail = company_license_detail
        self.allowed_limit = allowed_limit
        self.used_limit = used_limit
        self.unit = unit
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date