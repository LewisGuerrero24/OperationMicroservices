from Domain.Models.Module import Module as DomainModule
from Infrastructure.ModelsBD.Module import Module as DjangoModule

class ModuleMapper:

    @staticmethod
    def to_domain(model: DjangoModule) -> DomainModule:
        return DomainModule(
            name=model.name,
            description=model.description,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainModule) -> DjangoModule:
        model = DjangoModule(
            name=domain.name,
            description=domain.description,
            status=domain.status
        )
        # Las fechas las maneja automáticamente Django
        return model
