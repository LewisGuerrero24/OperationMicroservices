from Application.UseCases.PermitUseCase import PermitUseCase
from Domain.Ports.PermitRepository import PermitRepository
from Domain.Ports.SpacesRepository import SpacesRepository
from Domain.Ports.ModuleRepository import ModuleRepository
from Domain.Models.Permit import Permit

class Permit_Services(PermitUseCase):
    def __init__(self, permitRepository : PermitRepository, spacesRepository: SpacesRepository, moduleRepository: ModuleRepository):
        self._permitRepository = permitRepository
        self._spacesRepository = spacesRepository
        self._moduleRepository = moduleRepository

    def create(self, Permit_Data: dict) -> Permit:
        spaces = self._spacesRepository.get(Permit_Data['spaces'])
        module = self._moduleRepository.get(Permit_Data['module'])
        model_data = Permit(
            spaces=spaces,
            module=module,
            name=Permit_Data['name'],
            description=Permit_Data['description'],
            is_custom=Permit_Data['is_custom'],
            system_defined=Permit_Data['system_defined'],
            logical_route=Permit_Data['logical_route'],
            status=Permit_Data['status'],
            creation_date=Permit_Data['creation_date'],
            update_date=Permit_Data['update_date']
        )
        return self._permitRepository.create(model_data.__dict__)

    def get(self, Permit_Id: int) -> Permit:
        return self._permitRepository.get(Permit_Id)

    def update(self, Permit_Id: int, Permit_Data: dict) -> Permit:
        spaces = self._spacesRepository.get(Permit_Data['spaces'])
        module = self._moduleRepository.get(Permit_Data['module'])
        model_data = Permit(
            spaces=spaces,
            module=module,
            name=Permit_Data['name'],
            description=Permit_Data['description'],
            is_custom=Permit_Data['is_custom'],
            system_defined=Permit_Data['system_defined'],
            logical_route=Permit_Data['logical_route'],
            status=Permit_Data['status'],
            creation_date=Permit_Data['creation_date'],
            update_date=Permit_Data['update_date']
        )
        return self._permitRepository.update(Permit_Id, model_data.__dict__)

    def delete(self, Permit_Id: int) -> bool:
        return self._permitRepository.delete(Permit_Id)

    def list_all(self) -> list[Permit]:
        return self._permitRepository.list_all()

    def print_information(self, Permit_Data: dict) -> Permit:
        return self._permitRepository.print_information(Permit_Data)