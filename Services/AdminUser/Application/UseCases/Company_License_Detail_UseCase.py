from abc import ABC, abstractmethod
from Domain.Models.Company_license_detail import CompanyLicenseDetail

class CompanyLicenseUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> CompanyLicenseDetail:
        pass

    @abstractmethod
    def get(self, object_id: int) -> CompanyLicenseDetail:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> CompanyLicenseDetail:
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[CompanyLicenseDetail]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> CompanyLicenseDetail:
        pass

    class Meta:
        abstract = True
