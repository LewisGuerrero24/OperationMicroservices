from Domain.Ports.ServicesRepository import ServicesRepository
from Domain.Models.Services import Services 
from Infrastructure.ModelsBD.Services import Services as Servicesbd
from Infrastructure.Mappers.Services_mapper import ServicesMapper



class ServiceRepositoryImpl(ServicesRepository):
    def create(self, Services_data: dict) -> Services:
        model = Servicesbd.objects.create(**Services_data)
        return ServicesMapper.to_domain(model)

    def get(self, Services_id: int) -> Services:
        model = Servicesbd.objects.get(id=Services_id)
        return model

    def update(self, Services_id: int, Services_data: dict) -> Services:
        model = Servicesbd.objects.get(id=Services_id)
        for key, value in Services_data.items():
            setattr(model, key, value)
        model.save()
        return ServicesMapper.to_domain(model)

    def delete(self, Services_id:int) -> bool:
        model = Servicesbd.objects.get(id=Services_id)
        model.delete()
        return True

    def list_all(self) -> list[Services]:
        Services = Servicesbd.objects.all()
        return [ServicesMapper.to_domain(u) for u in Services]

    def print_information(self, Services_data: dict) -> Services:
        return Servicesbd(**Services_data)  