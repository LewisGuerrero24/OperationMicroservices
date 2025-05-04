from Application.UseCases.PermissionLevelUseCase import PermissionLevelUseCase
from Domain.Ports.PermissionLevelRepository import PermissionLevelRepository
from Domain.Models.Permission_level import PermissionLevel

class PermissionLevel_Services(PermissionLevelUseCase):
    def __init__(self, permissionLevelRepository : PermissionLevelRepository):
        self._permissionLevelRepository = permissionLevelRepository

    def create(self, PermissionLevel_Data: dict) -> PermissionLevel:
        return self._permissionLevelRepository.create(PermissionLevel_Data)

    def get(self, PermissionLevel_Id: int) -> PermissionLevel:
        return self._permissionLevelRepository.get(PermissionLevel_Id)

    def update(self, PermissionLevel_Id: int, PermissionLevel_Data: dict) -> PermissionLevel:
        return self._permissionLevelRepository.update(PermissionLevel_Id, PermissionLevel_Data)

    def delete(self, PermissionLevel_Id: int) -> bool:
        return self._permissionLevelRepository.delete(PermissionLevel_Id)

    def list_all(self) -> list[PermissionLevel]:
        return self._permissionLevelRepository.list_all()

    def print_information(self, PermissionLevel_Data: dict) -> PermissionLevel:
        return self._permissionLevelRepository.print_information(PermissionLevel_Data)