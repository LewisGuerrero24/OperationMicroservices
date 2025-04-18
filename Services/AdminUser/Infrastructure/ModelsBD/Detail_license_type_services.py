from django.db import models
from .License_type_services import License_type_services
from .Company_license_detail import Company_license_detail

class Detail_license_type_services(models.Model):
    license_type_services = models.ForeignKey(License_type_services, on_delete=models.PROTECT)
    company_license_detail = models.ForeignKey(Company_license_detail, on_delete=models.PROTECT)
    allowed_limit = models.PositiveIntegerField()
    used_limit = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50, default='registros')  # Unidad de medida (registros, GB, usuarios, etc.)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)