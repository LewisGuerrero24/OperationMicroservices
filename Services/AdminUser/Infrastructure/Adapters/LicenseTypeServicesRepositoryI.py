from Domain.Ports.License_TypeServices_Repository import LicenseTypeServicesRepository
from Domain.Models.License_type_services import LicenseTypeServices
from Infrastructure.ModelsBD.License_type_services import License_type_services as LicenseTypeServicesbd
from Infrastructure.Mappers.license_type_services_mapper import LicenseTypeServicesMapper


class LicenseTypeServiceRepositoryImpl(LicenseTypeServicesRepository):
    def create(self, LicenseTypeService_data: dict) -> LicenseTypeServices:
        model = LicenseTypeServicesbd.objects.create(**LicenseTypeService_data)
        return LicenseTypeServicesMapper.to_domain(model)

    def get(self, LicenseTypeService_id: int) -> LicenseTypeServices:
        model = LicenseTypeServicesbd.objects.get(id=LicenseTypeService_id)
        return model

    def update(self, LicenseTypeService_id: int, LicenseTypeService_data: dict) -> LicenseTypeServices:
        model = LicenseTypeServicesbd.objects.get(id=LicenseTypeService_id)
        for key, value in LicenseTypeService_data.items():
            setattr(model, key, value)
        model.save()
        return LicenseTypeServicesMapper.to_domain(model)

    def delete(self, LicenseTypeService_id:int) -> bool:
        model = LicenseTypeServicesbd.objects.get(id=LicenseTypeService_id)
        model.delete()
        return True

    def list_all(self) -> list[LicenseTypeServices]:
        LicenseTypeServices = LicenseTypeServicesbd.objects.all()
        return [LicenseTypeServicesMapper.to_domain(u) for u in LicenseTypeServices]

    def print_information(self, LicenseTypeService_data: dict) -> LicenseTypeServices:
        return LicenseTypeServicesbd(**LicenseTypeService_data)  # Puedes personalizar esto más adelante