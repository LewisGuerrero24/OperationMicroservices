from Domain.Ports.License_Type_Repository import LicenseTypeRepository
from Domain.Models.License_type import LicenseType 
from Infrastructure.ModelsBD.License_type import License_type as LicenseTypebd
from Infrastructure.Mappers.license_type_mapper import LicenseTypeMapper



class LicenseTyperRepositoryImpl(LicenseTypeRepository):
    def create(self, LicenseType_data: dict) -> LicenseType:
        model = LicenseTypebd.objects.create(**LicenseType_data)
        return LicenseTypeMapper.to_model(model)

    def get(self, LicenseType_id: int) -> LicenseType:
        model = LicenseTypebd.objects.get(id=LicenseType_id)
        return model

    def update(self, LicenseType_id: int, LicenseType_data: dict) -> LicenseType:
        model = LicenseTypebd.objects.get(id=LicenseType_id)
        for key, value in LicenseType_data.items():
            setattr(model, key, value)
        model.save()
        return LicenseTypeMapper.to_model(model)

    def delete(self, LicenseType_id:int) -> bool:
        model = LicenseTypebd.objects.get(id=LicenseType_id)
        model.delete()
        return True

    def list_all(self) -> list[LicenseType]:
        LicenseType = LicenseTypebd.objects.all()
        return [LicenseTypeMapper.to_model(u) for u in LicenseType]

    def print_information(self, LicenseType_data: dict) -> LicenseType:
        return LicenseTypebd(**LicenseType_data)  