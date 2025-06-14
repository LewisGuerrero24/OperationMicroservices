from Domain.Ports.CompanyRepository import CompanyRepository
from Domain.Models.Company import Company
from Infrastructure.ModelsBD.Company import Company as Companybd
from Infrastructure.Mappers.CompanyMapper import CompanyMapper


class CompanyRepositoryImpl(CompanyRepository):
    def create(self, company_data: dict) -> Company:
        model = Companybd.objects.create(**company_data)
        return CompanyMapper.to_model(model)

    def get(self, company_id: int) -> Company:
        model = Companybd.objects.get(id=company_id)
        return model

    def update(self, company_id: int, company_data: dict) -> Company:
        model = Companybd.objects.get(id=company_id)
        for key, value in company_data.items():
            setattr(model, key, value)
        model.save()
        return CompanyMapper.to_model(model)

    def delete(self, company_id:int) -> bool:
        model = Companybd.objects.get(id=company_id)
        model.delete()
        return True

    def list_all(self) -> list[Company]:
        Company = Companybd.objects.all()
        return [CompanyMapper.to_model(u) for u in Company]

    def print_information(self, company_data: dict) -> Company:
        return Companybd(**company_data)  