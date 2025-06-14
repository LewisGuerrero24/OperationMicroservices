from Domain.Ports.PermissionLevelRepository import PermissionLevelRepository
from Domain.Models.Permission_level import PermissionLevel
from Infrastructure.ModelsBD.Permission_level import Permission_level as PermissionLevelbd
from Infrastructure.Mappers.permission_level_mapper import PermissionLevelMapper


class PermissionLevelRepositoryImpl(PermissionLevelRepository):
    def create(self, PermissionLevel_data: dict) -> PermissionLevel:
        model = PermissionLevelbd.objects.create(**PermissionLevel_data)
        return PermissionLevelMapper.to_domain(model)

    def get(self, PermissionLevel_id: int) -> PermissionLevel:
        model = PermissionLevelbd.objects.get(id=PermissionLevel_id)
        return model

    def update(self, PermissionLevel_id: int, PermissionLevel_data: dict) -> PermissionLevel:
        model = PermissionLevelbd.objects.get(id=PermissionLevel_id)
        for key, value in PermissionLevel_data.items():
            setattr(model, key, value)
        model.save()
        return PermissionLevelMapper.to_domain(model)

    def delete(self, PermissionLevel_id:int) -> bool:
        model = PermissionLevelbd.objects.get(id=PermissionLevel_id)
        model.delete()
        return True

    def list_all(self) -> list[PermissionLevel]:
        PermissionLevel = PermissionLevelbd.objects.all()
        return [PermissionLevelMapper.to_domain(u) for u in PermissionLevel]

    def print_information(self, PermissionLevel_data: dict) -> PermissionLevel:
        return PermissionLevelbd(**PermissionLevel_data)  