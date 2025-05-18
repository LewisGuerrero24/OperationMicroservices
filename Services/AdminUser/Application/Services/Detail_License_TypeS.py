from Application.UseCases.DetailLicenseTypeServiceUseCase import DetailLicenseTypeServiceUseCase
from Domain.Ports.Detail_LicenseTypeRepository import DetailLicenseTypeServicesRepository
from Domain.Ports.CompanyLicenseDetailRepository import CompanyLicenseDetailRepository
from Domain.Ports.License_TypeServices_Repository import LicenseTypeServicesRepository
from Domain.Models.Detail_license_type_services import DetailLicenseTypeServices

class Detail_LicenseTypeS(DetailLicenseTypeServiceUseCase):
    def __init__(self, detailLicenseTypeServicesRepository: DetailLicenseTypeServicesRepository, companyLicenseDetailRepository: CompanyLicenseDetailRepository, licenseTypeServicesRepository: LicenseTypeServicesRepository):
        self._detailLicenseTypeServicesRepository = detailLicenseTypeServicesRepository
        self._companyLicenseDetailRepository = companyLicenseDetailRepository
        self._licenseTypeServicesRepository = licenseTypeServicesRepository

    def create(self, Company_License_DetailTypeService_data: dict) -> DetailLicenseTypeServices:
        company_license_detail = self._companyLicenseDetailRepository.get(Company_License_DetailTypeService_data['company_license_detail'])
        license_type_services = self._licenseTypeServicesRepository.get(Company_License_DetailTypeService_data['license_type_services'])
        data_model = DetailLicenseTypeServices(
            company_license_detail=company_license_detail,
            license_type_services=license_type_services,
            allowed_limit=Company_License_DetailTypeService_data['allowed_limit'],
            used_limit=Company_License_DetailTypeService_data['used_limit'],
            unit=Company_License_DetailTypeService_data['unit'],
            status=Company_License_DetailTypeService_data['status'],
            creation_date=Company_License_DetailTypeService_data['creation_date'],
            update_date=Company_License_DetailTypeService_data['update_date']
        )
        return self._detailLicenseTypeServicesRepository.create(data_model.__dict__)

    def get(self, Company_License_DetailTypeService_id: int) -> DetailLicenseTypeServices:
        return self._detailLicenseTypeServicesRepository.get(Company_License_DetailTypeService_id)

    def update(self, Company_License_DetailTypeService_id: int, Company_License_DetailTypeService_data: dict) -> DetailLicenseTypeServices:
        company_license_detail = self._companyLicenseDetailRepository.get(Company_License_DetailTypeService_data['company_license_detail'])
        license_type_services = self._licenseTypeServicesRepository.get(Company_License_DetailTypeService_data['license_type_services'])
        data_model = DetailLicenseTypeServices(
            company_license_detail=company_license_detail,
            license_type_services=license_type_services,
            allowed_limit=Company_License_DetailTypeService_data['allowed_limit'],
            used_limit=Company_License_DetailTypeService_data['used_limit'],
            unit=Company_License_DetailTypeService_data['unit'],
            status=Company_License_DetailTypeService_data['status'],
            creation_date=Company_License_DetailTypeService_data['creation_date'],
            update_date=Company_License_DetailTypeService_data['update_date']
        )
        return self._detailLicenseTypeServicesRepository.update(Company_License_DetailTypeService_id, data_model.__dict__)

    def delete(self, Company_License_DetailTypeService_id: int) -> bool:
        return self._detailLicenseTypeServicesRepository.delete(Company_License_DetailTypeService_id)

    def list_all(self) -> list[DetailLicenseTypeServices]:
        return self._detailLicenseTypeServicesRepository.list_all()

    def print_information(self, Company_License_DetailTypeService_data: dict) -> DetailLicenseTypeServices:
        return self._detailLicenseTypeServicesRepository.print_information(Company_License_DetailTypeService_data)