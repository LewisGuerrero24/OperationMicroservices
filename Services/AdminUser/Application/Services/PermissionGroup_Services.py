from Application.UseCases.PermissionGroupUseCase import PermissionGroupUseCase
from Domain.Ports.PermissionGroupRepository import PermissionGroupRepository
from Domain.Models.Permission_group import PermissionGroup

class PermissionGroup_Services(PermissionGroupUseCase):
    def __init__(self, permissionGroupRepository : PermissionGroupRepository):
        self._permissionGroupRepository = permissionGroupRepository

    def create(self, PermissionGroup_Data: dict) -> PermissionGroup:
        return self._permissionGroupRepository.create(PermissionGroup_Data)

    def get(self, PermissionGroup_Id: int) -> PermissionGroup:
        return self._permissionGroupRepository.get(PermissionGroup_Id)

    def update(self, PermissionGroup_Id: int, PermissionGroup_Data: dict) -> PermissionGroup:
        return self._permissionGroupRepository.update(PermissionGroup_Id, PermissionGroup_Data)

    def delete(self, PermissionGroup_Id: int) -> bool:
        return self._permissionGroupRepository.delete(PermissionGroup_Id)

    def list_all(self) -> list[PermissionGroup]:
        return self._permissionGroupRepository.list_all()

    def print_information(self, PermissionGroup_Data: dict) -> PermissionGroup:
        return self._permissionGroupRepository.print_information(PermissionGroup_Data)