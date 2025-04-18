from django.db import models
from Spaces import Spaces
from Module import Module

class Permit(models.Model):
    spaces = models.ForeignKey(Spaces, on_delete=models.PROTECT)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    is_custom = models.BooleanField(default=False)        # Si es un permiso creado por la empresa
    system_defined = models.BooleanField(default=False)   # True si lo define el sistema y no debe ser modificado
    logical_route = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

