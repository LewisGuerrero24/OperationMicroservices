from Domain.Ports.userRepository import UserRepository
from Domain.Models.System_User import SystemUsers
from Infrastructure.ModelsBD.System_users import System_users
from Infrastructure.Mappers.UserMapper import UserMapper
import uuid

class UserRepositoryImpl(UserRepository):
    def create(self, user_data: dict) -> SystemUsers:
        user_data['id'] = uuid.uuid4()
        model = System_users.objects.create(**user_data)
        return UserMapper.to_entity(model)

    def get(self, user_id: uuid.UUID) -> SystemUsers:
        model = System_users.objects.get(id=user_id)
        return UserMapper.to_entity(model)

    def update(self, user_id: uuid.UUID, user_data: dict) -> SystemUsers:
        model = System_users.objects.get(id=user_id)
        for key, value in user_data.items():
            setattr(model, key, value)
        model.save()
        return UserMapper.to_entity(model)

    def delete(self, user_id: uuid.UUID) -> bool:
        model = System_users.objects.get(id=user_id)
        model.delete()
        return True

    def list_all(self) -> list[SystemUsers]:
        users = System_users.objects.all()
        return [UserMapper.to_entity(u) for u in users]

    def print_information(self, user_data: dict) -> SystemUsers:
        return SystemUsers(**user_data)  # Puedes personalizar esto más adelante
