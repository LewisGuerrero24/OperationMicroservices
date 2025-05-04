from Domain.Models.System_User import SystemUsers
from Infrastructure.ModelsBD.System_users import System_users

class UserMapper:
    @staticmethod
    def to_entity(model: System_users) -> SystemUsers:
        return SystemUsers(
            id=model.id,
            full_name=model.full_name,
            username=model.username,
            email=model.email,
            password=model.password,
            is_superuser=model.is_superuser,
            last_login=model.last_login,
            status=model.status,
            creation_date=model.creation_date,
            update_date=model.update_date
        )

    @staticmethod
    def to_model(entity: SystemUsers) -> System_users:
        return System_users(
            id=entity.id,
            full_name=entity.full_name,
            username=entity.username,
            email=entity.email,
            password=entity.password,
            is_superuser=entity.is_superuser,
            last_login=entity.last_login,
            status=entity.status
        )
