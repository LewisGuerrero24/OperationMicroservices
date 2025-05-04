from typing import Optional
from Domain.Models.Detail_license_type_services import DetailLicenseTypeServices
from Mappers.license_type_services_mapper import LicenseTypeServicesMapper
from Mappers.CompanyLicenseDetailMapper import CompanyLicenseDetailMapper
from Infrastructure.ModelsBD.Detail_license_type_services import Detail_license_type_services


class DetailLicenseTypeServicesMapper:

    @staticmethod
    def to_domain(model: Detail_license_type_services) -> DetailLicenseTypeServices:
        return DetailLicenseTypeServices(
            license_type_services=LicenseTypeServicesMapper.to_domain(model.license_type_services),
            company_license_detail=CompanyLicenseDetailMapper.to_domain(model.company_license_detail),
            allowed_limit=model.allowed_limit,
            used_limit=model.used_limit,
            unit=model.unit,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DetailLicenseTypeServices) -> Detail_license_type_services:
        return Detail_license_type_services(
            license_type_services=LicenseTypeServicesMapper.to_model(domain.license_type_services),
            company_license_detail=CompanyLicenseDetailMapper.to_model(domain.company_license_detail),
            allowed_limit=domain.allowed_limit,
            used_limit=domain.used_limit,
            unit=domain.unit,
            status=domain.status,
            creation_date=domain.creation_date,
            update_date=domain.update_date
        )
