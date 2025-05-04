from Application.UseCases.GroupsUseCase import GroupsUseCase
from Domain.Ports.GroupsRepository import GroupsRepository
from Domain.Models.Groups import Groups

class Groups_Service(GroupsUseCase):
    def __init__(self, groupsRepository: GroupsRepository):
        self._groupsRepository = groupsRepository

    def create(self, group_Data: dict) -> Groups:
        return self._groupsRepository.create(group_Data)

    def get(self, Groups_Id: int) -> Groups:
        return self._groupsRepository.get(Groups_Id)

    def update(self, Groups_Id: int, group_Data: dict) -> Groups:
        return self._groupsRepository.update(Groups_Id, group_Data)

    def delete(self, Groups_Id: int) -> bool:
        return self._groupsRepository.delete(Groups_Id)

    def list_all(self) -> list[Groups]:
        return self._groupsRepository.list_all()

    def print_information(self, group_Data: dict) -> Groups:
        return self._groupsRepository.print_information(group_Data)