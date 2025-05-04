from django.db import models

class License_type(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True) # Ej: Básica, Media, Premium, personalizada, etc...
    description = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    support_level = models.CharField(max_length=50)  # Ej: "Soporte básico", "24/7", "Dedicado"
    duration_days = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'License_type'