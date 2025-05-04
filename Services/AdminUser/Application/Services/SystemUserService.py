from Application.UseCases.SystemUserUseCase import SystemUserUseCase
from Domain.Ports.SystemUserRepository import SystemUserRepository
from Domain.Models.System_User import SystemUsers

class SystemUser_Services(SystemUserUseCase):
    def __init__(self, systemUserRepository : SystemUserRepository):
        self._systemUserRepository = systemUserRepository

    def create(self, SystemUsers_Data: dict) -> SystemUsers:
        return self._systemUserRepository.create(SystemUsers_Data)

    def get(self, SystemUsers_Id: int) -> SystemUsers:
        return self._systemUserRepository.get(SystemUsers_Id)

    def update(self, SystemUsers_Id: int, SystemUsers_Data: dict) -> SystemUsers:
        return self._systemUserRepository.update(SystemUsers_Id, SystemUsers_Data)

    def delete(self, SystemUsers_Id: int) -> bool:
        return self._systemUserRepository.delete(SystemUsers_Id)

    def list_all(self) -> list[SystemUsers]:
        return self._systemUserRepository.list_all()

    def print_information(self, SystemUsers_Data: dict) -> SystemUsers:
        return self._systemUserRepository.print_information(SystemUsers_Data)