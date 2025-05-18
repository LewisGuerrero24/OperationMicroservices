from datetime import datetime
from typing import Optional
from Domain.Models.Company import Company


class CompanyLicenseDetail:
    def __init__(
        self, company: Company, overage_allowed: bool, overage_cost: Optional[float],
        start_date: datetime.date, cost: Optional[float], end_date: Optional[datetime.date],
        payment_reference: Optional[str], auto_renew: bool, observations: Optional[str],
        user_limit: int, status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.company = company
        self.overage_allowed = overage_allowed
        self.overage_cost = overage_cost
        self.start_date = start_date
        self.cost = cost
        self.end_date = end_date
        self.payment_reference = payment_reference
        self.auto_renew = auto_renew
        self.observations = observations
        self.user_limit = user_limit
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date