from Application.UseCases.Company_License_Detail_UseCase import CompanyLicenseUseCase
from Domain.Ports.CompanyLicenseDetailRepository import CompanyLicenseDetailRepository
from Domain.Ports.CompanyRepository import CompanyRepository
from Domain.Models.Company_license_detail import CompanyLicenseDetail


class Company_License_DetailService(CompanyLicenseUseCase):
    def __init__(self, companyLicenseDetailRepostory: CompanyLicenseDetail, companyRepository: CompanyRepository):
        self._companyLicenseDetailRepostory = companyLicenseDetailRepostory
        self._companyRepository = companyRepository

    def create(self, Company_License_Detail_data: dict) -> CompanyLicenseDetail:
        company = self._companyRepository.get(Company_License_Detail_data['company'])

        data_model = CompanyLicenseDetail(
            company=company,
            overage_allowed=Company_License_Detail_data.get('overage_allowed'),
            overage_cost=Company_License_Detail_data.get('overage_cost'),
            start_date=Company_License_Detail_data.get('start_date'),
            cost=Company_License_Detail_data.get('cost'),
            end_date=Company_License_Detail_data.get('end_date'),
            payment_reference=Company_License_Detail_data.get('payment_reference'),
            auto_renew=Company_License_Detail_data.get('auto_renew'),
            observations=Company_License_Detail_data.get('observations'),
            user_limit=Company_License_Detail_data.get('user_limit'),
            status=Company_License_Detail_data.get('status'),
            creation_date=Company_License_Detail_data.get('creation_date'),
            update_date=Company_License_Detail_data.get('update_date')
        )

        return self._companyLicenseDetailRepostory.create(data_model.__dict__)


    def get(self, Company_License_Detail_id: int) -> CompanyLicenseDetail:
        return self._companyLicenseDetailRepostory.get(Company_License_Detail_id)

    def update(self, Company_License_Detail_id: int, Company_License_Detail_data: dict) -> CompanyLicenseDetail:
        company = self._companyRepository.get(Company_License_Detail_data['company'])

        data_model = CompanyLicenseDetail(
            company=company,
            overage_allowed=Company_License_Detail_data.get('overage_allowed'),
            overage_cost=Company_License_Detail_data.get('overage_cost'),
            start_date=Company_License_Detail_data.get('start_date'),
            cost=Company_License_Detail_data.get('cost'),
            end_date=Company_License_Detail_data.get('end_date'),
            payment_reference=Company_License_Detail_data.get('payment_reference'),
            auto_renew=Company_License_Detail_data.get('auto_renew'),
            observations=Company_License_Detail_data.get('observations'),
            user_limit=Company_License_Detail_data.get('user_limit'),
            status=Company_License_Detail_data.get('status'),
            creation_date=Company_License_Detail_data.get('creation_date'),
            update_date=Company_License_Detail_data.get('update_date')
        )

        return self._companyLicenseDetailRepostory.update(Company_License_Detail_id, data_model.__dict__)

    def delete(self, Company_License_Detail_id: int) -> bool:
        return self._companyLicenseDetailRepostory.delete(Company_License_Detail_id)

    def list_all(self) -> list[CompanyLicenseDetail]:
        return self._companyLicenseDetailRepostory.list_all()

    def print_information(self, Company_License_Detail_data: dict) -> CompanyLicenseDetail:
        return self._companyLicenseDetailRepostory.print_information(Company_License_Detail_data)