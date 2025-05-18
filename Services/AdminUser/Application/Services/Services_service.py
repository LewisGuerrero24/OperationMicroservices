from Application.UseCases.ServicesUseCase import ServicesUseCase
from Domain.Ports.ServicesRepository import ServicesRepository
from Domain.Models.Services import Services

class Services_Services(ServicesUseCase):
    def __init__(self, serviceRepository : ServicesRepository):
        self._serviceRepository = serviceRepository

    def create(self, Services_Data: dict) -> Services:
        model_data  = Services(
            name=Services_Data['name'], 
            codeService=Services_Data['codeService'], 
            description=Services_Data['description'])

        return self._serviceRepository.create(model_data.__dict__)

    def get(self, Services_Id: int) -> Services:
        return self._serviceRepository.get(Services_Id)

    def update(self, Services_Id: int, Services_Data: dict) -> Services:
        return self._serviceRepository.update(Services_Id, Services_Data)

    def delete(self, Services_Id: int) -> bool:
        return self._serviceRepository.delete(Services_Id)

    def list_all(self) -> list[Services]:
        return self._serviceRepository.list_all()

    def print_information(self, Services_Data: dict) -> Services:
        return self._serviceRepository.print_information(Services_Data)