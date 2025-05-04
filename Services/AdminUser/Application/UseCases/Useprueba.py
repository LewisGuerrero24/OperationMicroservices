from Domain.Models.User import User
from abc import ABC, abstractmethod

class UserUseCase(ABC):

    @abstractmethod
    def ViewInformation(self,UserData)-> User:
        pass

    class Meta:
        abstract = True 
