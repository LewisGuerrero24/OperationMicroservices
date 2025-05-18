from Application.UseCases.SpacesUseCase import SpacesUseCase
from Domain.Ports.SpacesRepository import SpacesRepository
from Domain.Ports.CompanyRepository import CompanyRepository
from Domain.Models.Spaces import Spaces
import datetime

class Spaces_Services(SpacesUseCase):
    def __init__(self, spacesRepository : SpacesRepository, companyRepository : CompanyRepository):
        self._spacesRepository = spacesRepository
        self._companyRepository = companyRepository

    def create(self, Spaces_Data: dict) -> Spaces:
        company_space = self._companyRepository.get(Spaces_Data['company'])
        data_model = Spaces( 
        company=company_space,
        code=Spaces_Data['code'],
        name = Spaces_Data['name'],
        description = Spaces_Data['description'], 
        status = Spaces_Data['status'],
        creation_date=Spaces_Data['creation_date'],
        update_date=Spaces_Data ['update_date']
        )
        return self._spacesRepository.create(data_model.__dict__)
    
    def get(self, Spaces_Id: int) -> Spaces:
        return self._spacesRepository.get(Spaces_Id)

    def update(self, Spaces_Id: int, Spaces_Data: dict) -> Spaces:
        company_space = self._companyRepository.get(Spaces_Data['company'])
        data_model = Spaces( 
        company=company_space,
        code=Spaces_Data['code'],
        name = Spaces_Data['name'],
        description = Spaces_Data['description'], 
        status = Spaces_Data['status'],
        creation_date=Spaces_Data['creation_date'],
        update_date=Spaces_Data ['update_date']
        )
        return self._spacesRepository.update(Spaces_Id, data_model.__dict__)

    def delete(self, Spaces_Id: int) -> bool:
        return self._spacesRepository.delete(Spaces_Id)

    def list_all(self) -> list[Spaces]:
        return self._spacesRepository.list_all()

    def print_information(self, Spaces_Data: dict) -> Spaces:
        return self._spacesRepository.print_information(Spaces_Data)