from Application.UseCases.PermitUseCase import PermitUseCase
from Domain.Ports.PermitRepository import PermitRepository
from Domain.Models.Permit import Permit

class Permit_Services(PermitUseCase):
    def __init__(self, permitRepository : PermitRepository):
        self._permitRepository = permitRepository

    def create(self, Permit_Data: dict) -> Permit:
        return self._permitRepository.create(Permit_Data)

    def get(self, Permit_Id: int) -> Permit:
        return self._permitRepository.get(Permit_Id)

    def update(self, Permit_Id: int, Permit_Data: dict) -> Permit:
        return self._permitRepository.update(Permit_Id, Permit_Data)

    def delete(self, Permit_Id: int) -> bool:
        return self._permitRepository.delete(Permit_Id)

    def list_all(self) -> list[Permit]:
        return self._permitRepository.list_all()

    def print_information(self, Permit_Data: dict) -> Permit:
        return self._permitRepository.print_information(Permit_Data)