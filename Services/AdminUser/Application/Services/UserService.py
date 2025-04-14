from ..UseCases.UserUseCase  import UserUseCase
from Domain.Ports.userRepository import UserRepository
from Domain.Models.User import User

class UserService(UserUseCase):

    def __init__(self, userRepository : UserRepository):
        super().__init__()
        self._userRepository = userRepository

    @staticmethod
    def ViewInformation(self, UserData) -> User:
        # Aquí va la lógica concret
         UserD = User(
            id=UserData["id"],
            name=UserData["name"],
        )
         return UserRepository.Print_Information(UserD)
 