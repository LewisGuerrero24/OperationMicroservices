from Domain.Models.Permission_level import PermissionLevel as DomainPermissionLevel
from Infrastructure.ModelsBD.Permission_level import Permission_level as DjangoPermissionLevel

class PermissionLevelMapper:

    @staticmethod
    def to_domain(model: DjangoPermissionLevel) -> DomainPermissionLevel:
        return DomainPermissionLevel(
            name=model.name,
            level=model.level,
            description=model.description,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainPermissionLevel) -> DjangoPermissionLevel:
        model = DjangoPermissionLevel(
            name=domain.name,
            level=domain.level,
            description=domain.description,
            status=domain.status
        )
        return model
