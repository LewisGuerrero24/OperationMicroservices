# from ..UseCases.UserUseCase  import UserUseCase
# from Domain.Ports.userRepository import UserRepository
# from Domain.Models.User import User
# from Infrastructure.Mappers.UserMapper import UserMapper

# class UserService(UserUseCase):

#     def __init__(self, userRepository : UserRepository):
#         super().__init__()
#         self._userRepository = userRepository

#     def ViewInformation(self,UserData) -> User:
#         # Aquí va la lógica concret
#          UserD = User(
            
#             nombre=UserData["name"],
#             edad=UserData["edad"],
#         )
       
#          data =  self._userRepository.Print_Information(UserD)
#          print(""+data.nombre)
 