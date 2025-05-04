from Application.UseCases.UserUseCase import UserUseCase
from Domain.Ports.SystemUserRepository import SystemUserRepository
from Domain.Models.System_User import SystemUsers


class UserService(UserUseCase):
    def __init__(self, userRepository: SystemUserRepository):
        self._userRepository = userRepository

    def create(self, SystemUsers_data: dict) -> SystemUsers:
        return self._userRepository.create(SystemUsers_data)

    def get(self, SystemUsers_id: int) -> SystemUsers:
        return self._userRepository.get(SystemUsers_id)

    def update(self, SystemUsers_id: int, SystemUsers_data: dict) -> SystemUsers:
        return self._userRepository.update(SystemUsers_id, SystemUsers_data)

    def delete(self, SystemUsers_id: int) -> bool:
        return self._userRepository.delete(SystemUsers_id)

    def list_all(self) -> list[SystemUsers]:
        return self._userRepository.list_all()

    def print_information(self, SystemUsers_data: dict) -> SystemUsers:
        return self._userRepository.print_information(SystemUsers_data)
