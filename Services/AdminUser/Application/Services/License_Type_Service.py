from Application.UseCases.License_Type_UseCase import LicenseTypeUseCase
from Domain.Ports.License_Type_Repository import LicenseTypeRepository
from Domain.Models.License_type import LicenseType

class LicenseType_Service(LicenseTypeUseCase):
    def __init__(self, licenseTypeRepository: LicenseTypeRepository):
        self._licenseTypeRepository = licenseTypeRepository

    def create(self, LicenseType_Data: dict) -> LicenseType:
        return self._licenseTypeRepository.create(LicenseType_Data)

    def get(self, LicenseType_Id: int) -> LicenseType:
        return self._licenseTypeRepository.get(LicenseType_Id)

    def update(self, LicenseType_Id: int, LicenseType_Data: dict) -> LicenseType:
        return self._licenseTypeRepository.update(LicenseType_Id, LicenseType_Data)

    def delete(self, LicenseType_Id: int) -> bool:
        return self._licenseTypeRepository.delete(LicenseType_Id)

    def list_all(self) -> list[LicenseType]:
        return self._licenseTypeRepository.list_all()

    def print_information(self, LicenseType_Data: dict) -> LicenseType:
        return self._licenseTypeRepository.print_information(LicenseType_Data)