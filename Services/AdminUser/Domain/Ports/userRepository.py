from abc import ABC, abstractmethod
from ..Models.System_User import SystemUsers
from uuid import UUID

class UserRepository(ABC):

    @abstractmethod
    def create(self, user_data: dict) -> SystemUsers:
        """Crea un nuevo usuario y lo devuelve"""
        pass

    @abstractmethod
    def get(self, user_id: UUID) -> SystemUsers:
        """Obtiene un usuario por su ID"""
        pass

    @abstractmethod
    def update(self, user_id: UUID, user_data: dict) ->SystemUsers:
        """Actualiza los datos de un usuario existente"""
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> bool:
        """Elimina un usuario por su ID, devuelve True si fue exitoso"""
        pass

    @abstractmethod
    def list_all(self) -> list[SystemUsers]:
        """Devuelve una lista con todos los usuarios"""
        pass

    @abstractmethod
    def print_information(self, user_data: dict) -> SystemUsers:
        """Imprime o retorna información formateada del usuario"""
        pass

    class Meta:
        abstract = True

