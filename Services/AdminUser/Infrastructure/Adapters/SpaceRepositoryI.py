from Domain.Ports.SpacesRepository import SpacesRepository
from Domain.Models.Spaces import Spaces
from Infrastructure.ModelsBD.Spaces import Spaces as Spacesbd
from Infrastructure.Mappers.space_mapper import SpacesMapper


class SpaceRepositoryImpl(SpacesRepository):
    def create(self, space_data: dict) -> Spaces:
        model = Spacesbd.objects.create(**space_data)
        return SpacesMapper.to_domain(model)

    def get(self, space_id: int) -> Spaces:
        model = Spacesbd.objects.get(id=space_id)
        return model

    def update(self, space_id: int, space_data: dict) -> Spaces:
        model = Spacesbd.objects.get(id=space_id)
        for key, value in space_data.items():
            setattr(model, key, value)
        model.save()
        return SpacesMapper.to_domain(model)

    def delete(self, space_id:int) -> bool:
        model = Spacesbd.objects.get(id=space_id)
        model.delete()
        return True

    def list_all(self) -> list[Spaces]:
        spaces = Spacesbd.objects.all()
        return [SpacesMapper.to_domain(u) for u in spaces]

    def print_information(self, space_data: dict) -> Spaces:
        return Spacesbd(**space_data)  # Puedes personalizar esto más adelante