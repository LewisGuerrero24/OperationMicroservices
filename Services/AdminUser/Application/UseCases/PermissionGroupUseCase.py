from abc import ABC, abstractmethod
from Domain.Models.Permission_group import PermissionGroup

class PermissionGroupUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> PermissionGroup:
        pass

    @abstractmethod
    def get(self, object_id: int) -> PermissionGroup:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> PermissionGroup:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[PermissionGroup]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> PermissionGroup:
        pass

    class Meta:
        abstract = True
