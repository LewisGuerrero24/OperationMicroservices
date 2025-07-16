
from abc import ABC, abstractmethod
from ...Models.System_User import SystemUsers
from shared.DTO_Login import DTO_Login
from ...Models.response import GenericResponse

class SystemUsersLoginPort(ABC):
    @abstractmethod
    def login(self, login: DTO_Login) -> GenericResponse[SystemUsers]:
        pass

