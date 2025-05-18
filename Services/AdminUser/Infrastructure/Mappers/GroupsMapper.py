from Domain.Models.Groups import Groups as DomainGroups
from Infrastructure.ModelsBD.Groups import Groups as DjangoGroups
# Asumiendo que ya lo tienes o lo harás

class GroupsMapper:

    @staticmethod
    def to_domain(model: DjangoGroups) -> DomainGroups:
        return DomainGroups(
            spaces=model.spaces,
            code=model.code,
            name=model.name,
            description=model.description,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(domain: DomainGroups) -> DjangoGroups:
        return DjangoGroups(
            spaces=domain.spaces,
            code=domain.code,
            name=domain.name,
            description=domain.description,
            status=domain.status,
            creation_date=domain.creation_date,
            update_date=domain.update_date
        )
