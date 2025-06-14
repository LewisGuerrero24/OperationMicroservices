from Domain.Ports.ModuleRepository import ModuleRepository
from Domain.Models.Module import Module
from Infrastructure.ModelsBD.Module import Module as Modulebd
from Infrastructure.Mappers.module_mapper import ModuleMapper


class ModuleRepositoryImpl(ModuleRepository):
    def create(self, Module_data: dict) -> Module:
        model = Modulebd.objects.create(**Module_data)
        return ModuleMapper.to_model(model)

    def get(self, Module_id: int) -> Module:
        model = Modulebd.objects.get(id=Module_id)
        return model

    def update(self, Module_id: int, Module_data: dict) -> Module:
        model = Modulebd.objects.get(id=Module_id)
        for key, value in Module_data.items():
            setattr(model, key, value)
        model.save()
        return ModuleMapper.to_model(model)

    def delete(self, Module_id:int) -> bool:
        model = Modulebd.objects.get(id=Module_id)
        model.delete()
        return True

    def list_all(self) -> list[Module]:
        Module = Modulebd.objects.all()
        return [ModuleMapper.to_model(u) for u in Module]

    def print_information(self, Module_data: dict) -> Module:
        return Modulebd(**Module_data)  