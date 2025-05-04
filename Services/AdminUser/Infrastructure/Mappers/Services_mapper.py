from datetime import datetime
from typing import Optional
from Domain.Models.Services import Services as DomainServices
from Infrastructure.ModelsBD.Services import Services as DjangoServices

class ServicesMapper:
    @staticmethod
    def to_domain(service: DjangoServices) -> DomainServices:
        return DomainServices(
            name=service.name,
            code_service=service.codeService,
            description=service.description,
            status=service.status,
            creation_date=service.creation_date,
            update_date=service.update_date
        )

    @staticmethod
    def to_django(service: DomainServices) -> DjangoServices:
        return DjangoServices(
            name=service.name,
            codeService=service.code_service,
            description=service.description,
            status=service.status,
            creation_date=service.creation_date,
            update_date=service.update_date
        )
