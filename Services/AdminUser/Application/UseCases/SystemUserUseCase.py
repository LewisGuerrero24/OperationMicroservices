from abc import ABC, abstractmethod
from ...Domain.Models.System_User import SystemUsers

class SystemUserUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> SystemUsers:
        pass

    @abstractmethod
    def get(self, object_id: int) -> SystemUsers:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> SystemUsers:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[SystemUsers]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> SystemUsers:
        pass

    class Meta:
        abstract = True
