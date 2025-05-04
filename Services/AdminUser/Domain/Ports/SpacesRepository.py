from abc import ABC, abstractmethod
from ..Models.Spaces import Spaces

class SpacesRepository(ABC):

    @abstractmethod
    def create(self, data: dict) -> Spaces:
        pass

    @abstractmethod
    def get(self, object_id: int) -> Spaces:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> Spaces:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[Spaces]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> Spaces:
        pass

    class Meta:
        abstract = True
