from Domain.Ports.User_Groups_Repository import UserGroupsRepository
from Domain.Models.User_groups import UserGroups
from Infrastructure.ModelsBD.User_groups import User_groups as UserGroupsbd
from Infrastructure.Mappers.user_groups_mapper import UserGroupsMapper


class UserGroupRepositoryImpl(UserGroupsRepository):
    def create(self, UserGroups_data: dict) -> UserGroups:
        model = UserGroupsbd.objects.create(**UserGroups_data)
        return UserGroupsMapper.to_domain(model)

    def get(self, UserGroups_id: int) -> UserGroups:
        model = UserGroupsbd.objects.get(id=UserGroups_id)
        return model

    def update(self, UserGroups_id: int, UserGroups_data: dict) -> UserGroups:
        model = UserGroupsbd.objects.get(id=UserGroups_id)
        for key, value in UserGroups_data.items():
            setattr(model, key, value)
        model.save()
        return UserGroupsMapper.to_domain(model)

    def delete(self, UserGroups_id:int) -> bool:
        model = UserGroupsbd.objects.get(id=UserGroups_id)
        model.delete()
        return True

    def list_all(self) -> list[UserGroups]:
        UserGroups = UserGroupsbd.objects.all()
        return [UserGroupsMapper.to_domain(u) for u in UserGroups]

    def print_information(self, UserGroups_data: dict) -> UserGroups:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        return UserGroupsbd(**UserGroups_data)              