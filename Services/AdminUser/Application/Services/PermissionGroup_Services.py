from Application.UseCases.PermissionGroupUseCase import PermissionGroupUseCase
from Domain.Ports.PermissionGroupRepository import PermissionGroupRepository
from Domain.Ports.GroupsRepository import GroupsRepository
from Domain.Ports.PermissionLevelRepository import PermissionLevelRepository
from Domain.Ports.PermitRepository import PermitRepository
from Domain.Models.Permission_group import PermissionGroup

class PermissionGroup_Services(PermissionGroupUseCase):
    def __init__(self, permissionGroupRepository : PermissionGroupRepository, groupsRepository: GroupsRepository, permissionLevelRepository: PermissionLevelRepository, permitRepository: PermitRepository):
        self._permissionGroupRepository = permissionGroupRepository
        self._groupsRepository = groupsRepository
        self._permissionLevelRepository = permissionLevelRepository
        self._permitRepository = permitRepository

    def create(self, PermissionGroup_Data: dict) -> PermissionGroup:
        Group_Data = self._groupsRepository.get(PermissionGroup_Data['group'])
        PermissionLevel_Data = self._permissionLevelRepository.get(PermissionGroup_Data['permission_level'])
        Permit_Data = self._permitRepository.get(PermissionGroup_Data['permit'])
        model_data = PermissionGroup(
            group=Group_Data,
            permission_level=PermissionLevel_Data,
            permit=Permit_Data,
            status=PermissionGroup_Data['status'],
            creation_date=PermissionGroup_Data['creation_date'],
            update_date=PermissionGroup_Data['update_date']      
        )
        return self._permissionGroupRepository.create(model_data.__dict__)

    def get(self, PermissionGroup_Id: int) -> PermissionGroup:
        return self._permissionGroupRepository.get(PermissionGroup_Id)

    def update(self, PermissionGroup_Id: int, PermissionGroup_Data: dict) -> PermissionGroup:
        Group_Data = self._groupsRepository.get(PermissionGroup_Data['group'])
        PermissionLevel_Data = self._permissionLevelRepository.get(PermissionGroup_Data['permission_level'])
        Permit_Data = self._permitRepository.get(PermissionGroup_Data['permit'])
        model_data = PermissionGroup(
            group=Group_Data,
            permission_level=PermissionLevel_Data,
            permit=Permit_Data,
            status=PermissionGroup_Data['status'],
            creation_date=PermissionGroup_Data['creation_date'],
            update_date=PermissionGroup_Data['update_date']      
        )   
        return self._permissionGroupRepository.update(PermissionGroup_Id, model_data.__dict__)

    def delete(self, PermissionGroup_Id: int) -> bool:
        return self._permissionGroupRepository.delete(PermissionGroup_Id)

    def list_all(self) -> list[PermissionGroup]:
        return self._permissionGroupRepository.list_all()

    def print_information(self, PermissionGroup_Data: dict) -> PermissionGroup:
        return self._permissionGroupRepository.print_information(PermissionGroup_Data)