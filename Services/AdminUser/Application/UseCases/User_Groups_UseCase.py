from abc import ABC, abstractmethod
from ...Domain.Models.User_groups import UserGroups

class UserGroupsUseCase(ABC):

    @abstractmethod
    def create(self, data: dict) -> UserGroups:
        pass

    @abstractmethod
    def get(self, object_id: int) -> UserGroups:
        pass

    @abstractmethod
    def update(self, object_id: int, data: dict) -> UserGroups: 
        pass

    @abstractmethod
    def delete(self, object_id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> list[UserGroups]:
        pass

    @abstractmethod
    def print_information(self, data: dict) -> UserGroups:
        pass

    class Meta:
        abstract = True
