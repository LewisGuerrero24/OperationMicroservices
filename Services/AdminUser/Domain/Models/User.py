from django.db import models
from dataclasses import dataclass

class User:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad