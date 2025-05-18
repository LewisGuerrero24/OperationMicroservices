from Domain.Ports.PermissionUserRepository import PermissionUserRepository
from Domain.Models.Permission_user import PermissionUser
from Infrastructure.ModelsBD.Permission_user import Permission_user as PermissionUserbd
from Infrastructure.Mappers.permission_user_mapper import PermissionUserMapper


class PermissionUserRepositoryImpl(PermissionUserRepository):
    def create(self, Permission_user_data: dict) -> PermissionUser:
        model = PermissionUserbd.objects.create(**Permission_user_data)
        return PermissionUserMapper.to_model(model)

    def get(self, Permission_user_id: int) -> PermissionUser:
        model = PermissionUserbd.objects.get(id=Permission_user_id)
        return model

    def update(self, Permission_user_id: int, Permission_user_data: dict) -> PermissionUser:
        model = PermissionUserbd.objects.get(id=Permission_user_id)
        for key, value in Permission_user_data.items():
            setattr(model, key, value)
        model.save()
        return PermissionUserMapper.to_model(model)

    def delete(self, Permission_user_id:int) -> bool:
        model = PermissionUserbd.objects.get(id=Permission_user_id)
        model.delete()
        return True

    def list_all(self) -> list[PermissionUser]:
        Permission_user = PermissionUserbd.objects.all()
        return [PermissionUserMapper.to_model(u) for u in Permission_user]

    def print_information(self, Permission_user_data: dict) -> PermissionUser:
        return PermissionUserbd(**Permission_user_data)         