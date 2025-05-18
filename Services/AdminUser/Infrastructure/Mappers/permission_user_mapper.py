from Domain.Models.Permission_user import PermissionUser as DomainPermissionUser
from Infrastructure.ModelsBD.Permission_user import Permission_user as DjangoPermissionUser

from Infrastructure.Mappers.permission_level_mapper import PermissionLevelMapper
from Infrastructure.Mappers.permit_mapper import PermitMapper
from Infrastructure.Mappers.system_users_mapper import SystemUsersMapper

class PermissionUserMapper:

    @staticmethod
    def to_domain(model: DjangoPermissionUser) -> DomainPermissionUser:
        return DomainPermissionUser(
            system_user=model.system_user,
            permission_level=model.permission_level,
            permit=model.permit,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainPermissionUser) -> DjangoPermissionUser:
        model = DjangoPermissionUser(
            system_user=domain.system_user,
            permission_level=domain.permission_level,
            permit=domain.permit,
            status=domain.status
        )
        return model
