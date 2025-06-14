from Application.UseCases.CompanyUseCase import CompanyUseCase
from Domain.Ports.CompanyRepository import CompanyRepository
from Domain.Models.Company import Company


class CompanyService(CompanyUseCase):
    def __init__(self, companyRepository: CompanyRepository):
        self._companyRepostory = companyRepository

    def create(self, Company_data: dict) -> Company:
        return self._companyRepostory.create(Company_data)

    def get(self, company_id: int) -> Company:
        return self._companyRepostory.get(company_id)

    def update(self, company_id: int, company_data: dict) -> Company:
        return self._companyRepostory.update(company_id, company_data)

    def delete(self, company_id: int) -> bool:
        return self._companyRepostory.delete(company_id)

    def list_all(self) -> list[Company]:
        return self._companyRepostory.list_all()

    def print_information(self, company_data: dict) -> Company:
        return self._companyRepostory.print_information(company_data)