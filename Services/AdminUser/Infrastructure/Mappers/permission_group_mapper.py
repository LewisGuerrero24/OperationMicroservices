from Domain.Models.Permission_group import PermissionGroup as DomainPermissionGroup
from Infrastructure.ModelsBD.Permission_group import Permission_group as DjangoPermissionGroup
from Mappers.GroupsMapper import GroupMapper
from Mappers.permission_level_mapper import PermissionLevelMapper
from Mappers.permit_mapper import PermitMapper
from Mappers.GroupsMapper import GroupsMapper

class PermissionGroupMapper:

    @staticmethod
    def to_domain(model: DjangoPermissionGroup) -> DomainPermissionGroup:
        return DomainPermissionGroup(
            group=GroupsMapper.to_domain(model.group),
            permission_level=PermissionLevelMapper.to_domain(model.permission_level),
            permit=PermitMapper.to_domain(model.permit),
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainPermissionGroup) -> DjangoPermissionGroup:
        model = DjangoPermissionGroup(
            group=GroupsMapper.to_model(domain.group),
            permission_level=PermissionLevelMapper.to_model(domain.permission_level),
            permit=PermitMapper.to_model(domain.permit),
            status=domain.status
        )
        return model
