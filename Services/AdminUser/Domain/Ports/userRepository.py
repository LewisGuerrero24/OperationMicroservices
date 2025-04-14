from ..Models.User import User
from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def Print_Information(self,UserData)-> User:
        pass

    class Meta:
        abstract = True 
