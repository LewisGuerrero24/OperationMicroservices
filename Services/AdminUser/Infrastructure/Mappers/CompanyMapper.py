from Domain.Models.Company import Company as CompanyEntity
from Infrastructure.ModelsBD.Company import Company as CompanyModel

class CompanyMapper:
    @staticmethod
    def to_entity(model: CompanyModel) -> CompanyEntity:
        return CompanyEntity(
            name=model.name,
            legal_name=model.legal_name,
            nit=model.nit,
            country=model.country,
            location=model.location,
            phone=model.phone,
            email=model.email,
            postal_code=model.postal_code,
            website=model.website,
            contact_name=model.contact_name,
            contact_phone=model.contact_phone,
            contact_email=model.contact_email,
            notes=model.notes,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(entity: CompanyEntity) -> CompanyModel:
        return CompanyModel(
            name=entity.name,
            legal_name=entity.legal_name,
            nit=entity.nit,
            country=entity.country,
            location=entity.location,
            phone=entity.phone,
            email=entity.email,
            postal_code=entity.postal_code,
            website=entity.website,
            contact_name=entity.contact_name,
            contact_phone=entity.contact_phone,
            contact_email=entity.contact_email,
            notes=entity.notes,
            status=entity.status
        )
