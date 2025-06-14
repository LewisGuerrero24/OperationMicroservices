from Domain.Ports.CompanyLicenseDetailRepository import CompanyLicenseDetailRepository
from Domain.Models.Company_license_detail import CompanyLicenseDetail
from Infrastructure.ModelsBD.Company_license_detail import Company_license_detail as CompanyLicenseDetailbd
from Infrastructure.Mappers.CompanyLicenseDetailMapper import CompanyLicenseDetailMapper


class CompanyLicenseDetailRepositoryImpl(CompanyLicenseDetailRepository):
    def create(self, CompanyLicenseDetail_data: dict) -> CompanyLicenseDetail:
        model = CompanyLicenseDetailbd.objects.create(**CompanyLicenseDetail_data)
        return CompanyLicenseDetailMapper.to_model(model)

    def get(self, CompanyLicenseDetail_id: int) -> CompanyLicenseDetail:
        model = CompanyLicenseDetailbd.objects.get(id=CompanyLicenseDetail_id)
        return model

    def update(self, CompanyLicenseDetail_id: int, CompanyLicenseDetail_data: dict) -> CompanyLicenseDetail:
        model = CompanyLicenseDetailbd.objects.get(id=CompanyLicenseDetail_id)
        for key, value in CompanyLicenseDetail_data.items():
            setattr(model, key, value)
        model.save()
        return CompanyLicenseDetailMapper.to_model(model)

    def delete(self, CompanyLicenseDetail_id:int) -> bool:
        model = CompanyLicenseDetailbd.objects.get(id=CompanyLicenseDetail_id)
        model.delete()
        return True

    def list_all(self) -> list[CompanyLicenseDetail]:
        CompanyLicenseDetail = CompanyLicenseDetailbd.objects.all()
        return [CompanyLicenseDetailMapper.to_model(u) for u in CompanyLicenseDetail]

    def print_information(self, CompanyLicenseDetail_data: dict) -> CompanyLicenseDetail:
        return CompanyLicenseDetailbd(**CompanyLicenseDetail_data)  