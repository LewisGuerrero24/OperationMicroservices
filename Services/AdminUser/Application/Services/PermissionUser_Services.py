from Application.UseCases.PermissionUserUseCase import PermissionUserUseCase
from Domain.Ports.PermissionUserRepository import PermissionUserRepository
from Domain.Models.Permission_user import PermissionUser

class PermissionUser_Services(PermissionUserUseCase):
    def __init__(self, permissionUserRepository : PermissionUserRepository):
        self._permissionUserRepository = permissionUserRepository

    def create(self, PermissionUser_Data: dict) -> PermissionUser:
        return self._permissionUserRepository.create(PermissionUser_Data)

    def get(self, PermissionUser_Id: int) -> PermissionUser:
        return self._permissionUserRepository.get(PermissionUser_Id)

    def update(self, PermissionUser_Id: int, PermissionUser_Data: dict) -> PermissionUser:
        return self._permissionUserRepository.update(PermissionUser_Id, PermissionUser_Data)

    def delete(self, PermissionUser_Id: int) -> bool:
        return self._permissionUserRepository.delete(PermissionUser_Id)

    def list_all(self) -> list[PermissionUser]:
        return self._permissionUserRepository.list_all()

    def print_information(self, PermissionUser_Data: dict) -> PermissionUser:
        return self._permissionUserRepository.print_information(PermissionUser_Data)