from Application.UseCases.Company_License_Detail_UseCase import CompanyLicenseUseCase
from Domain.Ports.CompanyLicenseDetailRepository import CompanyLicenseDetailRepository
from Domain.Models.Company_license_detail import CompanyLicenseDetail


class Company_License_DetailService(CompanyLicenseUseCase):
    def __init__(self, companyLicenseDetailRepostory: CompanyLicenseDetail):
        self._companyLicenseDetailRepostory = companyLicenseDetailRepostory

    def create(self, Company_License_Detail_data: dict) -> CompanyLicenseDetail:
        return self._companyLicenseDetailRepostory.create(Company_License_Detail_data)

    def get(self, Company_License_Detail_id: int) -> CompanyLicenseDetail:
        return self._companyLicenseDetailRepostory.get(Company_License_Detail_id)

    def update(self, Company_License_Detail_id: int, Company_License_Detail_data: dict) -> CompanyLicenseDetail:
        return self._companyLicenseDetailRepostory.update(Company_License_Detail_id, Company_License_Detail_data)

    def delete(self, Company_License_Detail_id: int) -> bool:
        return self._companyLicenseDetailRepostory.delete(Company_License_Detail_id)

    def list_all(self) -> list[CompanyLicenseDetail]:
        return self._companyLicenseDetailRepostory.list_all()

    def print_information(self, Company_License_Detail_data: dict) -> CompanyLicenseDetail:
        return self._companyLicenseDetailRepostory.print_information(Company_License_Detail_data)