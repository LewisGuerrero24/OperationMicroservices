from abc import ABC, abstractmethod
from ...Domain.Models.License_type import LicenseType

class LicenseTypeUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> LicenseType:
        pass

    @abstractmethod
    def get(self, object_id: int) -> LicenseType:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> LicenseType:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[LicenseType]:
        pass

    @abstractmethod
    def print_information(self, data: dict) ->LicenseType:
        pass

    class Meta:
        abstract = True
