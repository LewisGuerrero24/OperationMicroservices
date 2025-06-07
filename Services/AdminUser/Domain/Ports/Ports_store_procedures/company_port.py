from abc import ABC, abstractmethod
from ...Models.Company import Company
from ...Models.response import GenericResponse

class CompanyRepositoryPort(ABC):
    @abstractmethod
    def create_company(self, company: Company) -> GenericResponse[int]:
        pass
