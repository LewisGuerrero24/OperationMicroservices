from Application.UseCases.PermissionUserUseCase import PermissionUserUseCase
from Domain.Ports.PermissionUserRepository import PermissionUserRepository
from Domain.Ports.SystemUserRepository import SystemUserRepository
from Domain.Ports.PermissionLevelRepository import PermissionLevelRepository
from Domain.Ports.PermitRepository import PermitRepository
from Domain.Models.Permission_user import PermissionUser
from Infrastructure.Mappers.system_users_mapper import SystemUsersMapper

class PermissionUser_Services(PermissionUserUseCase):
    def __init__(self, permissionUserRepository : PermissionUserRepository, systemUserRepository: SystemUserRepository, permissionLevelRepository: PermissionLevelRepository, permitRepository: PermitRepository):
        self._permissionUserRepository = permissionUserRepository
        self._systemUserRepository = systemUserRepository
        self._permissionLevelRepository = permissionLevelRepository
        self._permitRepository = permitRepository

    def create(self, PermissionUser_Data: dict) -> PermissionUser:
        systemUser_Data = self._systemUserRepository.get(PermissionUser_Data['system_user'])
        PermissionLevel = self._permissionLevelRepository.get(PermissionUser_Data['permission_level'])
        Permit_Data = self._permitRepository.get(PermissionUser_Data['permit'])
        model_data_User = SystemUsersMapper.to_django(systemUser_Data)
        model_data = PermissionUser(
            system_user=model_data_User,
            permission_level=PermissionLevel,
            permit=Permit_Data,
            status=PermissionUser_Data['status'],
            creation_date=PermissionUser_Data['creation_date'],
            update_date=PermissionUser_Data['update_date']      
        )              
        return self._permissionUserRepository.create(model_data.__dict__)

    def get(self, PermissionUser_Id: int) -> PermissionUser:
        return self._permissionUserRepository.get(PermissionUser_Id)

    def update(self, PermissionUser_Id: int, PermissionUser_Data: dict) -> PermissionUser:
        systemUser_Data = self._systemUserRepository.get(PermissionUser_Data['system_user'])
        PermissionLevel = self._permissionLevelRepository.get(PermissionUser_Data['permission_level'])
        Permit_Data = self._permitRepository.get(PermissionUser_Data['permit'])
        model_data_User = SystemUsersMapper.to_django(systemUser_Data)
        model_data = PermissionUser(
            system_user=model_data_User,
            permission_level=PermissionLevel,
            permit=Permit_Data,
            status=PermissionUser_Data['status'],
            creation_date=PermissionUser_Data['creation_date'],
            update_date=PermissionUser_Data['update_date']      
        ) 
        return self._permissionUserRepository.update(PermissionUser_Id, model_data.__dict__)

    def delete(self, PermissionUser_Id: int) -> bool:
        return self._permissionUserRepository.delete(PermissionUser_Id)

    def list_all(self) -> list[PermissionUser]:
        return self._permissionUserRepository.list_all()

    def print_information(self, PermissionUser_Data: dict) -> PermissionUser:
        return self._permissionUserRepository.print_information(PermissionUser_Data)