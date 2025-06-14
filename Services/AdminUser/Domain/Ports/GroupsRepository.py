from abc import ABC, abstractmethod
from ..Models.Groups import Groups

class GroupsRepository(ABC):

    @abstractmethod
    def create(self, data: dict) -> Groups:
        pass

    @abstractmethod
    def get(self, object_id: int) -> Groups:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> Groups:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[Groups]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> Groups:
        pass

    class Meta:
        abstract = True
