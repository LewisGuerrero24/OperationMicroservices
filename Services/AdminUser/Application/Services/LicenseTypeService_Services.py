from Application.UseCases.License_TypeServices_UseCase import LicenseTypeServicesUseCase
from Domain.Ports.License_TypeServices_Repository import LicenseTypeServicesRepository
from Domain.Models.License_type_services import LicenseTypeServices

class LicenseTypeServiceS(LicenseTypeServicesUseCase):
    def __init__(self, licenseTypeServicesRepository: LicenseTypeServicesRepository):
        self._licenseType_ServiceRepository = licenseTypeServicesRepository

    def create(self, LicenseTypeService_Data: dict) -> LicenseTypeServices:
        return self._licenseType_ServiceRepository.create(LicenseTypeService_Data)

    def get(self, LicenseTypeServices_Id: int) -> LicenseTypeServices:
        return self._licenseType_ServiceRepository.get(LicenseTypeServices_Id)

    def update(self, LicenseTypeServices_Id: int, LicenseTypeService_Data: dict) -> LicenseTypeServices:
        return self._licenseType_ServiceRepository.update(LicenseTypeServices_Id, LicenseTypeService_Data)

    def delete(self, LicenseTypeServices_Id: int) -> bool:
        return self._licenseType_ServiceRepository.delete(LicenseTypeServices_Id)

    def list_all(self) -> list[LicenseTypeServices]:
        return self._licenseType_ServiceRepository.list_all()

    def print_information(self, LicenseTypeService_Data: dict) -> LicenseTypeServices:
        return self._licenseType_ServiceRepository.print_information(LicenseTypeService_Data)