from Domain.Models.License_type_services import LicenseTypeServices as DomainLicenseTypeServices
from Infrastructure.ModelsBD.License_type_services import License_type_services as DjangoLicenseTypeServices

from Mappers.license_type_mapper import LicenseTypeMapper
from Mappers.Services_mapper import ServicesMapper


class LicenseTypeServicesMapper:

    @staticmethod
    def to_domain(model: DjangoLicenseTypeServices) -> DomainLicenseTypeServices:
        return DomainLicenseTypeServices(
            license_type=LicenseTypeMapper.to_domain(model.license_type),
            service=ServicesMapper.to_domain(model.service),
            max_records=model.max_records,
            duration_days=model.duration_days,
            custom_limit_note=model.custom_limit_note,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainLicenseTypeServices) -> DjangoLicenseTypeServices:
        return DjangoLicenseTypeServices(
            license_type=LicenseTypeMapper.to_model(domain.license_type),
            service=ServicesMapper.to_model(domain.service),
            max_records=domain.max_records,
            duration_days=domain.duration_days,
            custom_limit_note=domain.custom_limit_note,
            status=domain.status,
            creation_date=domain.creation_date,
            update_date=domain.update_date
        )
