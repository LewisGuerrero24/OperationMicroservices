from abc import ABC, abstractmethod
from ...Domain.Models.Services import Services

class ServicesUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> Services:
        pass

    @abstractmethod
    def get(self, object_id: int) -> Services:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> Services:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[Services]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> Services:
        pass

    class Meta:
        abstract = True
