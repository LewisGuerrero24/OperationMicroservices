
from abc import ABC, abstractmethod
from Domain.Models.Detail_license_type_services  import DetailLicenseTypeServices

class DetailLicenseTypeServiceUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> DetailLicenseTypeServices:
        pass

    @abstractmethod
    def get(self, object_id: int) -> DetailLicenseTypeServices:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> DetailLicenseTypeServices:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[DetailLicenseTypeServices]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> DetailLicenseTypeServices:
        pass

    class Meta:
        abstract = True