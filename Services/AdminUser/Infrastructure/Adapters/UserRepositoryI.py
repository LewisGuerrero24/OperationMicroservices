from Domain.Ports.userRepository import UserRepository
from ..ModelsBD.UserModelBd import UserModelBd
from Domain.Models.User import User
from ..Mappers.UserMapper import UserMapper

class UserRepositoryI(UserRepository):
    def __init__(self,userModelBd = UserModelBd()):
        super().__init__()
        self._userModelBd = userModelBd
     
        
    def Print_Information(self,UserData)-> User:
        user_model = UserMapper.to_model(UserData)
        user_model.save()
        return UserMapper.to_domain(user_model)