from abc import ABC, abstractmethod
from ...Domain.Models.Module import Module

class ModuleUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> Module:
        pass

    @abstractmethod
    def get(self, object_id: int) -> Module:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> Module:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[Module]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> Module:
        pass

    class Meta:
        abstract = True
