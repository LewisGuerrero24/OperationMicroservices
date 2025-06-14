from Domain.Ports.PermitRepository import PermitRepository
from Domain.Models.Permit import Permit
from Infrastructure.ModelsBD.Permit import Permit as Permitbd
from Infrastructure.Mappers.permit_mapper import PermitMapper


class PermitRepositoryImpl(PermitRepository):
    def create(self, Permit_data: dict) -> Permit:
        model = Permitbd.objects.create(**Permit_data)
        return PermitMapper.to_domain(model)

    def get(self, Permit_id: int) -> Permit:
        model = Permitbd.objects.get(id=Permit_id)
        return model

    def update(self, Permit_id: int, Permit_data: dict) -> Permit:
        model = Permitbd.objects.get(id=Permit_id)
        for key, value in Permit_data.items():
            setattr(model, key, value)
        model.save()
        return PermitMapper.to_domain(model)

    def delete(self, Permit_id:int) -> bool:
        model = Permitbd.objects.get(id=Permit_id)
        model.delete()
        return True

    def list_all(self) -> list[Permit]:
        Permit = Permitbd.objects.all()
        return [PermitMapper.to_domain(u) for u in Permit]

    def print_information(self, Permit_data: dict) -> Permit:
        return Permitbd(**Permit_data)  