from Domain.Models.License_type import LicenseType as DomainLicenseType
from Infrastructure.ModelsBD.License_type import License_type as DjangoLicenseType

class LicenseTypeMapper:

    @staticmethod
    def to_domain(model: DjangoLicenseType) -> DomainLicenseType:
        return DomainLicenseType(
            name=model.name,
            description=model.description,
            price=float(model.price),  # Decimal -> float
            support_level=model.support_level,
            duration_days=model.duration_days,
            max_users=model.max_users,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainLicenseType) -> DjangoLicenseType:
        model = DjangoLicenseType(
            name=domain.name,
            description=domain.description,
            price=domain.price,  # float -> DecimalField (Django se encarga)
            support_level=domain.support_level,
            duration_days=domain.duration_days,
            max_users=domain.max_users,
            status=domain.status
        )
        # Las fechas de creación/actualización las maneja Django automáticamente
        return model
