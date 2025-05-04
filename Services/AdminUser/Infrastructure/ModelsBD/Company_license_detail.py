from django.db import models
from .Company import Company

class Company_license_detail(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    overage_allowed = models.BooleanField(default=False)
    overage_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    start_date = models.DateField() 
    cost = models.DecimalField(max_digits=20, decimal_places=6, null=True)
    end_date = models.DateField(null=True)
    payment_reference = models.CharField(max_length=100, null=True)
    auto_renew = models.BooleanField(default=False)
    observations = models.CharField(max_length=200, null=True)
    user_limit = models.PositiveIntegerField(default=0)

    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'Company_license_detail'
