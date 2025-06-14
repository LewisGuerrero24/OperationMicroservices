from Application.UseCases.UserUseCase import UserUseCase
from Domain.Ports.SystemUserRepository import SystemUserRepository
from Domain.Ports.SpacesRepository import SpacesRepository
from Domain.Models.System_User import SystemUsers
from Domain.Dto.UserDto import systemUsersDto
from uuid import UUID
import uuid
import datetime

class UserService(UserUseCase):
    def __init__(self, userRepository: SystemUserRepository, spacesRepository: SpacesRepository):
        self._userRepository = userRepository
        self._spacesRepository = spacesRepository

    def create(self, system_users_data: dict) -> systemUsersDto:
        spaces_user = self._spacesRepository.get(system_users_data['spaces'])
        data_id = uuid.uuid4()
        data_model = SystemUsers( 
            id=data_id,
            spaces=spaces_user,
            full_name=system_users_data['full_name'],
            username=system_users_data['username'],
            email=system_users_data['email'],
            password=system_users_data['password'],
            is_superuser=system_users_data['is_superuser'],
            last_login=system_users_data['last_login'],
            status=system_users_data['status'],
            creation_date=system_users_data['creation_date'],
            update_date=system_users_data['update_date']
        )

        return self._userRepository.create(data_model)



    def get(self, SystemUsers_id: UUID) -> SystemUsers:
        return self._userRepository.get(SystemUsers_id)

    def update(self, SystemUsers_id: UUID, system_users_data: dict) -> systemUsersDto:
        spaces_user = self._spacesRepository.get(system_users_data['spaces'])
        # saveSpace = SpacesMapper.to_django(spaces_user)
        data_model = SystemUsers( 
            id=SystemUsers_id,
            spaces=spaces_user,
            full_name=system_users_data['full_name'],
            username=system_users_data['username'],
            email=system_users_data['email'],
            password=system_users_data['password'],
            is_superuser=system_users_data['is_superuser'],
            last_login=system_users_data['last_login'],
            status=system_users_data['status'],
            creation_date=system_users_data['creation_date'],
            update_date=system_users_data['update_date']
        )
        updated_user = self._userRepository.update(SystemUsers_id,data_model.__dict__)
        return updated_user

    def delete(self, SystemUsers_id: UUID) -> bool:
        return self._userRepository.delete(SystemUsers_id)

    def list_all(self) -> list[SystemUsers]:
        return self._userRepository.list_all()

    def print_information(self, SystemUsers_data: dict) -> SystemUsers:
        return self._userRepository.print_information(SystemUsers_data)
