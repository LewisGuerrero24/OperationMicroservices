from Domain.Models.Permission_user import PermissionUser as DomainPermissionUser
from Infrastructure.ModelsBD.Permission_user import Permission_user as DjangoPermissionUser

from Infrastructure.Mappers.permission_level_mapper import PermissionLevelMapper
from Infrastructure.Mappers.permit_mapper import PermitMapper
from Infrastructure.Mappers.system_users_mapper import SystemUsersMapper

class PermissionUserMapper:

    @staticmethod
    def to_domain(model: DjangoPermissionUser) -> DomainPermissionUser:
        return DomainPermissionUser(
            system_user=SystemUsersMapper.to_domain(model.system_user),
            permission_level=PermissionLevelMapper.to_domain(model.permission_level),
            permit=PermitMapper.to_domain(model.permit),
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainPermissionUser) -> DjangoPermissionUser:
        model = DjangoPermissionUser(
            system_user=SystemUsersMapper.to_model(domain.system_user),
            permission_level=PermissionLevelMapper.to_model(domain.permission_level),
            permit=PermitMapper.to_model(domain.permit),
            status=domain.status
        )
        return model
