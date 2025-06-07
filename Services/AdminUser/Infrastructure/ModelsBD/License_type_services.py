from django.db import models
from .License_type import License_type
from .Services import Services
from django.utils import timezone

class License_type_services(models.Model):
    license_type = models.ForeignKey(License_type, on_delete=models.PROTECT)
    service = models.ForeignKey(Services, on_delete=models.PROTECT)
    max_records = models.PositiveIntegerField(null=False)
    duration_days = models.PositiveIntegerField(null=False)
    custom_limit_note = models.CharField(max_length=255, null=True) 
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'License_type_services'