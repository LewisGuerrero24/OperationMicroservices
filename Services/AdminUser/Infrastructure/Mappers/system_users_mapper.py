from typing import Optional
from uuid import UUID
from datetime import datetime
from Domain.Models.System_User import SystemUsers as DomainSystemUsers
from Infrastructure.ModelsBD.System_users import System_users as DjangoSystemUsers

class SystemUsersMapper:
    @staticmethod
    def to_domain(user: DjangoSystemUsers) -> DomainSystemUsers:
        return DomainSystemUsers(
            id=user.id,
            spaces=user.spaces,
            full_name=user.full_name,
            username=user.username,
            email=user.email,
            password=user.password,
            is_superuser=user.is_superuser,
            last_login=user.last_login,
            status=user.status,
            creation_date=user.creation_date,
            update_date=user.update_date
        )

    @staticmethod
    def to_django(user: DomainSystemUsers) -> DjangoSystemUsers:
        return DjangoSystemUsers(
            id=user.id,
            spaces=user.spaces,
            full_name=user.full_name,
            username=user.username,
            email=user.email,
            password=user.password,
            is_superuser=user.is_superuser,
            last_login=user.last_login,
            status=user.status,
            creation_date=user.creation_date,
            update_date=user.update_date
        )
