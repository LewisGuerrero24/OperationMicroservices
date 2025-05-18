from abc import ABC, abstractmethod
from Domain.Models.System_User import SystemUsers
from uuid import UUID

class UserUseCase(ABC):

    @abstractmethod
    def create(self, SystemUsers_data: dict) -> SystemUsers:
        """Crea un nuevo usuario y lo devuelve"""
        pass

    @abstractmethod
    def get(self, SystemUsers_id: UUID) -> SystemUsers:
        """Obtiene un usuario por su ID"""
        pass

    @abstractmethod
    def update(self, SystemUsers_id: UUID, SystemUsers_data: dict) -> SystemUsers:
        """Actualiza los datos de un usuario existente"""
        pass

    @abstractmethod
    def delete(self, SystemUsers_id: UUID) -> bool:
        """Elimina un usuario por su ID, devuelve True si fue exitoso"""
        pass

    @abstractmethod
    def list_all(self) -> list[SystemUsers]:
        """Devuelve una lista con todos los usuarios"""
        pass

    @abstractmethod
    def print_information(self, SystemUsers_data: dict) -> SystemUsers:
        """Imprime o retorna información formateada del usuario"""
        pass

    class Meta:
        abstract = True

