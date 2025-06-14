from abc import ABC, abstractmethod
from ..Models.Permission_user import PermissionUser

class PermissionUserRepository(ABC):

    @abstractmethod
    def create(self, data: dict) -> PermissionUser:
        pass

    @abstractmethod
    def get(self, object_id: int) -> PermissionUser:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> PermissionUser:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[PermissionUser]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> PermissionUser:
        pass

    class Meta:
        abstract = True
