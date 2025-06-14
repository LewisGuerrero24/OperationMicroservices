from Application.UseCases.Module_UseCase import ModuleUseCase
from Domain.Ports.ModuleRepository import ModuleRepository
from Domain.Models.Module import Module

class Module_Services(ModuleUseCase):
    def __init__(self, moduleRepository: ModuleRepository):
        self._moduleRepository = moduleRepository

    def create(self, Module_Data: dict) -> Module:
        return self._moduleRepository.create(Module_Data)

    def get(self, Module_Id: int) -> Module:
        return self._moduleRepository.get(Module_Id)

    def update(self, Module_Id: int, Module_Data: dict) -> Module:
        return self._moduleRepository.update(Module_Id, Module_Data)

    def delete(self, Module_Id: int) -> bool:
        return self._moduleRepository.delete(Module_Id)

    def list_all(self) -> list[Module]:
        return self._moduleRepository.list_all()

    def print_information(self, Module_Data: dict) -> Module:
        return self._moduleRepository.print_information(Module_Data)