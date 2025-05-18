from Application.UseCases.License_TypeServices_UseCase import LicenseTypeServicesUseCase
from Domain.Ports.License_TypeServices_Repository import LicenseTypeServicesRepository
from Domain.Ports.License_Type_Repository import LicenseTypeRepository
from Domain.Ports.ServicesRepository import ServicesRepository
from Domain.Models.License_type_services import LicenseTypeServices

class LicenseTypeServiceS(LicenseTypeServicesUseCase):
    def __init__(self, licenseTypeServicesRepository: LicenseTypeServicesRepository, licenseTypeRepository: LicenseTypeRepository, serviceRepository: ServicesRepository):
        self._licenseType_ServiceRepository = licenseTypeServicesRepository
        self._licenseTypeRepository = licenseTypeRepository
        self._serviceRepository = serviceRepository

    def create(self, LicenseTypeService_Data: dict) -> LicenseTypeServices:
        license_type = self._licenseTypeRepository.get(LicenseTypeService_Data['license_type'])
        service = self._serviceRepository.get(LicenseTypeService_Data['service'])
        data_model = LicenseTypeServices(
            license_type=license_type,
            service=service,
            max_records=LicenseTypeService_Data['max_records'],
            duration_days=LicenseTypeService_Data['duration_days'],
            custom_limit_note=LicenseTypeService_Data['custom_limit_note'],
            status=LicenseTypeService_Data['status'],
            creation_date=LicenseTypeService_Data['creation_date'],
            update_date=LicenseTypeService_Data['update_date']
        )
        return self._licenseType_ServiceRepository.create(data_model.__dict__)

    def get(self, LicenseTypeServices_Id: int) -> LicenseTypeServices:
        return self._licenseType_ServiceRepository.get(LicenseTypeServices_Id)

    def update(self, LicenseTypeServices_Id: int, LicenseTypeService_Data: dict) -> LicenseTypeServices:
        license_type = self._licenseTypeRepository.get(LicenseTypeService_Data['license_type'])
        service = self._serviceRepository.get(LicenseTypeService_Data['service'])
        data_model = LicenseTypeServices(
            license_type=license_type,
            service=service,
            max_records=LicenseTypeService_Data['max_records'],
            duration_days=LicenseTypeService_Data['duration_days'],
            custom_limit_note=LicenseTypeService_Data['custom_limit_note'],
            status=LicenseTypeService_Data['status'],
            creation_date=LicenseTypeService_Data['creation_date'],
            update_date=LicenseTypeService_Data['update_date']
        )
        return self._licenseType_ServiceRepository.update(LicenseTypeServices_Id, data_model.__dict__)

    def delete(self, LicenseTypeServices_Id: int) -> bool:
        return self._licenseType_ServiceRepository.delete(LicenseTypeServices_Id)

    def list_all(self) -> list[LicenseTypeServices]:
        return self._licenseType_ServiceRepository.list_all()

    def print_information(self, LicenseTypeService_Data: dict) -> LicenseTypeServices:
        return self._licenseType_ServiceRepository.print_information(LicenseTypeService_Data)