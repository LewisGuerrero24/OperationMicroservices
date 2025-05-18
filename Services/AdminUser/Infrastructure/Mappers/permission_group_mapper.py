from Domain.Models.Permission_group import PermissionGroup as DomainPermissionGroup
from Infrastructure.ModelsBD.Permission_group import Permission_group as DjangoPermissionGroup


class PermissionGroupMapper:

    @staticmethod
    def to_domain(model: DjangoPermissionGroup) -> DomainPermissionGroup:
        return DomainPermissionGroup(
            group=model.group,
            permission_level=model.permission_level,
            permit=model.permit,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainPermissionGroup) -> DjangoPermissionGroup:
        model = DjangoPermissionGroup(
            group=domain.group,
            permission_level=domain.permission_level,
            permit=domain.permit,
            status=domain.status
        )
        return model
