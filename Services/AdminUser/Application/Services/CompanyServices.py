# Application/UseCases/create_company_use_case.py

from Domain.Ports.Ports_store_procedures.company_port import CompanyRepositoryPort
from Domain.Models.response import GenericResponse
from Domain.Models.Company import Company
from ..UseCases.Company_repository import CompanyUseCasePort
from ..DTOs.CompanyDTO import CompanyDTO
from Application.Mappers.mapper import dto_to_model

class CreateCompanyUseCase(CompanyUseCasePort):
        
    def __init__(self, company_repository: CompanyRepositoryPort):
        self.company_repository = company_repository

    def create_company(self, company_dto: CompanyDTO) -> GenericResponse[int]:
        company: Company = dto_to_model(company_dto, Company)
        return self.company_repository.create_company(company)
    
    def delete_company(self, company_id: int) -> GenericResponse[bool]:
        return self.company_repository.delete_company(company_id)
