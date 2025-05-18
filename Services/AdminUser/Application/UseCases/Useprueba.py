from Domain.Models.User_Kafka import User
from abc import ABC, abstractmethod

class UserUseCase(ABC):

    @abstractmethod
    def ViewInformation(self,UserData)-> User:
        pass

    class Meta:
        abstract = True 
