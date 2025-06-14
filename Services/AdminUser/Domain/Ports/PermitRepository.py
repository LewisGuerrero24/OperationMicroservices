from abc import ABC, abstractmethod
from ..Models.Permit import Permit

class PermitRepository(ABC):

    @abstractmethod
    def create(self, data: dict) -> Permit:
        pass

    @abstractmethod
    def get(self, object_id: int) -> Permit:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> Permit:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[Permit]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> Permit:
        pass

    class Meta:
        abstract = True
