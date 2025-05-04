from abc import ABC, abstractmethod
from ...Domain.Models.License_type_services import LicenseTypeServices

class LicenseTypeServicesUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> LicenseTypeServices:
        pass

    @abstractmethod
    def get(self, object_id: int) -> LicenseTypeServices:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> LicenseTypeServices:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[LicenseTypeServices]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> LicenseTypeServices:
        pass

    class Meta:
        abstract = True
