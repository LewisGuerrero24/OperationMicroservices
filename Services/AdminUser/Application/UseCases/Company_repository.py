# Application/Interfaces/company_use_case_port.py

from abc import ABC, abstractmethod
from ..DTOs.CompanyDTO import CompanyDTO
from Domain.Models.response import GenericResponse

class CompanyUseCasePort(ABC):
    @abstractmethod
    def create_company(self, company_dto: CompanyDTO) -> GenericResponse[int]:
        pass

    @abstractmethod
    def delete_company(self, company_id: int) -> GenericResponse[bool]:
        pass