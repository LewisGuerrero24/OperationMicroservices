from Application.UseCases.SpacesUseCase import SpacesUseCase
from Domain.Ports.SpacesRepository import SpacesRepository
from Domain.Models.Spaces import Spaces

class Spaces_Services(SpacesUseCase):
    def __init__(self, spacesRepository : SpacesRepository):
        self._spacesRepository = spacesRepository

    def create(self, Spaces_Data: dict) -> Spaces:
        return self._spacesRepository.create(Spaces_Data)

    def get(self, Spaces_Id: int) -> Spaces:
        return self._spacesRepository.get(Spaces_Id)

    def update(self, Spaces_Id: int, Spaces_Data: dict) -> Spaces:
        return self._spacesRepository.update(Spaces_Id, Spaces_Data)

    def delete(self, Spaces_Id: int) -> bool:
        return self._spacesRepository.delete(Spaces_Id)

    def list_all(self) -> list[Spaces]:
        return self._spacesRepository.list_all()

    def print_information(self, Spaces_Data: dict) -> Spaces:
        return self._spacesRepository.print_information(Spaces_Data)