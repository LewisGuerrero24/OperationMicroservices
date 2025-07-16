from abc import ABC, abstractmethod
from Application.DTOs.DTO_LoginResponse import DTO_LoginResponse
from Domain.Models.response import GenericResponse
from shared.DTO_Login import DTO_Login

class SystemUsersUseCasePort(ABC):
    @abstractmethod
    def login(self, DTO_Login: DTO_Login) -> GenericResponse[DTO_LoginResponse]:
        pass
