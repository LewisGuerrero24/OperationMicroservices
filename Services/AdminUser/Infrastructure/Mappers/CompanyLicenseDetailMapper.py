from Domain.Models.Company_license_detail import CompanyLicenseDetail
from Infrastructure.ModelsBD.Company_license_detail import Company_license_detail
from Infrastructure.Mappers.CompanyMapper import CompanyMapper  # Este mapper debe existir

class CompanyLicenseDetailMapper:
    @staticmethod
    def to_entity(model: Company_license_detail) -> CompanyLicenseDetail:
        return CompanyLicenseDetail(
            company=CompanyMapper.to_entity(model.company),
            overage_allowed=model.overage_allowed,
            overage_cost=float(model.overage_cost) if model.overage_cost is not None else None,
            start_date=model.start_date,
            cost=float(model.cost) if model.cost is not None else None,
            end_date=model.end_date,
            payment_reference=model.payment_reference,
            auto_renew=model.auto_renew,
            observations=model.observations,
            user_limit=model.user_limit,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(entity: CompanyLicenseDetail) -> Company_license_detail:
        return Company_license_detail(
            company=CompanyMapper.to_model(entity.company),
            overage_allowed=entity.overage_allowed,
            overage_cost=entity.overage_cost,
            start_date=entity.start_date,
            cost=entity.cost,
            end_date=entity.end_date,
            payment_reference=entity.payment_reference,
            auto_renew=entity.auto_renew,
            observations=entity.observations,
            user_limit=entity.user_limit,
            status=entity.status
        )
