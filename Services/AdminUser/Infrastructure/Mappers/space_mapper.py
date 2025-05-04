from datetime import datetime
from typing import Optional
from Domain.Models.Spaces import Spaces as DomainSpaces
from Infrastructure.ModelsBD.Spaces import Spaces as DjangoSpaces

class SpacesMapper:
    @staticmethod
    def to_domain(spaces: DjangoSpaces) -> DomainSpaces:
        return DomainSpaces(
            company=spaces.company,
            code=spaces.code,
            name=spaces.name,
            description=spaces.description,
            status=spaces.status,
            creation_date=spaces.creation_date,
            update_date=spaces.update_date
        )

    @staticmethod
    def to_django(spaces: DomainSpaces) -> DjangoSpaces:
        return DjangoSpaces(
            company=spaces.company,
            code=spaces.code,
            name=spaces.name,
            description=spaces.description,
            status=spaces.status,
            creation_date=spaces.creation_date,
            update_date=spaces.update_date
        )
