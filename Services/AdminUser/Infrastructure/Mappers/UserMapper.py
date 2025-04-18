# from Domain.Models.User import User
# from Infrastructure.ModelsBD.UserModelBd import UserModelBd

# class UserMapper:
#     @staticmethod
#     def to_domain(user_model: UserModelBd) -> User:
#         return User(nombre=user_model.name, edad= user_model.edad)

#     @staticmethod
#     def to_model(user: User) -> UserModelBd:
#         model = UserModelBd()
#         model.name = user.nombre
#         model.edad = user.edad
#         return model