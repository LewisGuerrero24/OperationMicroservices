from abc import ABC, abstractmethod
from Domain.Models.Permission_level import PermissionLevel

class PermissionLevelUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> PermissionLevel:
        pass

    @abstractmethod
    def get(self, object_id: int) -> PermissionLevel:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> PermissionLevel:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[PermissionLevel]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> PermissionLevel:
        pass

    class Meta:
        abstract = True
