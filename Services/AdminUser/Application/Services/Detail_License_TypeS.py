from Application.UseCases.DetailLicenseTypeServiceUseCase import DetailLicenseTypeServiceUseCase
from Domain.Ports.Detail_LicenseTypeRepository import DetailLicenseTypeServicesRepository
from Domain.Models.Detail_license_type_services import DetailLicenseTypeServices

class Detail_LicenseTypeS(DetailLicenseTypeServiceUseCase):
    def __init__(self, detailLicenseTypeServicesRepository: DetailLicenseTypeServicesRepository):
        self._detailLicenseTypeServicesRepository = detailLicenseTypeServicesRepository

    def create(self, Company_License_DetailTypeService_data: dict) -> DetailLicenseTypeServices:
        return self._detailLicenseTypeServicesRepository.create(Company_License_DetailTypeService_data)

    def get(self, Company_License_DetailTypeService_id: int) -> DetailLicenseTypeServices:
        return self._detailLicenseTypeServicesRepository.get(Company_License_DetailTypeService_id)

    def update(self, Company_License_DetailTypeService_id: int, Company_License_DetailTypeService_data: dict) -> DetailLicenseTypeServices:
        return self._detailLicenseTypeServicesRepository.update(Company_License_DetailTypeService_id, Company_License_DetailTypeService_data)

    def delete(self, Company_License_DetailTypeService_id: int) -> bool:
        return self._detailLicenseTypeServicesRepository.delete(Company_License_DetailTypeService_id)

    def list_all(self) -> list[DetailLicenseTypeServices]:
        return self._detailLicenseTypeServicesRepository.list_all()

    def print_information(self, Company_License_DetailTypeService_data: dict) -> DetailLicenseTypeServices:
        return self._detailLicenseTypeServicesRepository.print_information(Company_License_DetailTypeService_data)