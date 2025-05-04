from datetime import datetime
from typing import Optional
from Domain.Models import Permit as DomainPermit, Module, Spaces
from Infrastructure.ModelsBD.Permit import Permit as DjangoPermit

class PermitMapper:
    @staticmethod
    def to_domain(permit: DjangoPermit) -> DomainPermit:
        return DomainPermit(
            spaces=permit.spaces,
            module=permit.module,
            name=permit.name,
            description=permit.description,
            is_custom=permit.is_custom,
            system_defined=permit.system_defined,
            logical_route=permit.logical_route,
            status=permit.status,
            creation_date=permit.creation_date,
            update_date=permit.update_date
        )

    @staticmethod
    def to_django(permit: DomainPermit) -> DjangoPermit:
        return DjangoPermit(
            spaces=permit.spaces,
            module=permit.module,
            name=permit.name,
            description=permit.description,
            is_custom=permit.is_custom,
            system_defined=permit.system_defined,
            logical_route=permit.logical_route,
            status=permit.status,
            creation_date=permit.creation_date,
            update_date=permit.update_date
        )
