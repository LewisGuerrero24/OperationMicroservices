from datetime import datetime
from Domain.Models.User_groups import UserGroups as DomainUserGroups
from Infrastructure.ModelsBD.User_groups import User_groups as DjangoUserGroups

class UserGroupsMapper:
    @staticmethod
    def to_domain(user_group: DjangoUserGroups) -> DomainUserGroups:
        return DomainUserGroups(
            system_user=user_group.system_user,
            group=user_group.group,
            status=user_group.status,
            creation_date=user_group.creation_date,
            update_date=user_group.update_date
        )

    @staticmethod
    def to_django(user_group: DomainUserGroups) -> DjangoUserGroups:
        return DjangoUserGroups(
            system_user=user_group.system_user,
            group=user_group.group,
            status=user_group.status,
            creation_date=user_group.creation_date,
            update_date=user_group.update_date
        )
