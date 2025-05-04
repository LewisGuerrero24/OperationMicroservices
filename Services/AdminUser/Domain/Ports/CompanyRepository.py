from abc import ABC, abstractmethod
from ..Models.Company import Company

class CompanyRepository(ABC):

    @abstractmethod
    def create(self, company_data: dict) -> Company:
        """Crea un nuevo usuario y lo devuelve"""
        pass

    @abstractmethod
    def get(self, company_id: int) -> Company:
        """Obtiene un usuario por su ID"""
        pass

    @abstractmethod
    def update(self, company_id: int, company_data: dict) -> Company:
        """Actualiza los datos de un usuario existente"""
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """Elimina un usuario por su ID, devuelve True si fue exitoso"""
        pass

    @abstractmethod
    def list_all(self) -> list[Company]:
        """Devuelve una lista con todos los usuarios"""
        pass

    @abstractmethod
    def print_information(self,Company_data: dict) -> Company:
        """Imprime o retorna información formateada del usuario"""
        pass

    class Meta:
        abstract = True


