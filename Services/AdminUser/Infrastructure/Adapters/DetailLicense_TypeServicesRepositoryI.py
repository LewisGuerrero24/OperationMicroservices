from Domain.Ports.Detail_LicenseTypeRepository import DetailLicenseTypeServicesRepository
from Domain.Models.Detail_license_type_services import DetailLicenseTypeServices 
from Infrastructure.ModelsBD.Detail_license_type_services import Detail_license_type_services as DetailLicenseTypeServicesbd
from Infrastructure.Mappers.DetailLicenseTypeServicesMapper import DetailLicenseTypeServicesMapper



class DetailLicenseTypeServiceRepositoryImpl(DetailLicenseTypeServicesRepository):
    def create(self, DetailLicenseTypeServices_data: dict) -> DetailLicenseTypeServices:
        model = DetailLicenseTypeServicesbd.objects.create(**DetailLicenseTypeServices_data)
        return DetailLicenseTypeServicesMapper.to_model(model)

    def get(self, DetailLicenseTypeServices_id: int) -> DetailLicenseTypeServices:
        model = DetailLicenseTypeServicesbd.objects.get(id=DetailLicenseTypeServices_id)
        return model

    def update(self, DetailLicenseTypeServices_id: int, DetailLicenseTypeServices_data: dict) -> DetailLicenseTypeServices:
        model = DetailLicenseTypeServicesbd.objects.get(id=DetailLicenseTypeServices_id)
        for key, value in DetailLicenseTypeServices_data.items():
            setattr(model, key, value)
        model.save()
        return DetailLicenseTypeServicesMapper.to_model(model)

    def delete(self, DetailLicenseTypeServices_id:int) -> bool:
        model = DetailLicenseTypeServicesbd.objects.get(id=DetailLicenseTypeServices_id)
        model.delete()
        return True

    def list_all(self) -> list[DetailLicenseTypeServices]:
        DetailLicenseTypeServices = DetailLicenseTypeServicesbd.objects.all()
        return [DetailLicenseTypeServicesMapper.to_model(u) for u in DetailLicenseTypeServices]

    def print_information(self, DetailLicenseTypeServices_data: dict) -> DetailLicenseTypeServices:
        return DetailLicenseTypeServicesbd(**DetailLicenseTypeServices_data)  