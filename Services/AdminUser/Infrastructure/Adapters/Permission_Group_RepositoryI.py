from Domain.Ports.PermissionGroupRepository import PermissionGroupRepository
from Domain.Models.Permission_group import PermissionGroup
from Infrastructure.ModelsBD.Permission_group import Permission_group as PermissionGroupbd
from Infrastructure.Mappers.permission_group_mapper import PermissionGroupMapper


class PermissionGroupRepositoryImpl(PermissionGroupRepository):
    def create(self, PermissionGroup_data: dict) -> PermissionGroup:
        model = PermissionGroupbd.objects.create(**PermissionGroup_data)
        return PermissionGroupMapper.to_model(model)

    def get(self, PermissionGroup_id: int) -> PermissionGroup:
        model = PermissionGroupbd.objects.get(id=PermissionGroup_id)
        return model

    def update(self, PermissionGroup_id: int, PermissionGroup_data: dict) -> PermissionGroup:
        model = PermissionGroupbd.objects.get(id=PermissionGroup_id)
        for key, value in PermissionGroup_data.items():
            setattr(model, key, value)
        model.save()
        return PermissionGroupMapper.to_model(model)

    def delete(self, PermissionGroup_id:int) -> bool:
        model = PermissionGroupbd.objects.get(id=PermissionGroup_id)
        model.delete()
        return True

    def list_all(self) -> list[PermissionGroup]:
        PermissionGroup = PermissionGroupbd.objects.all()
        return [PermissionGroupMapper.to_model(u) for u in PermissionGroup]

    def print_information(self, PermissionGroup_data: dict) -> PermissionGroup:
        return PermissionGroupbd(**PermissionGroup_data)  