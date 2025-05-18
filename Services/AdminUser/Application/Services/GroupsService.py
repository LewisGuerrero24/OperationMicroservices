from Application.UseCases.GroupsUseCase import GroupsUseCase
from Domain.Ports.GroupsRepository import GroupsRepository
from Domain.Ports.SpacesRepository import SpacesRepository
from Domain.Models.Groups import Groups

class Groups_Service(GroupsUseCase):
    def __init__(self, groupsRepository: GroupsRepository, spacesRepository: SpacesRepository):
        self._groupsRepository = groupsRepository
        self._spacesRepository = spacesRepository

    def create(self, group_Data: dict) -> Groups:
        spaces = self._spacesRepository.get(group_Data['spaces'])
        model_data = Groups(
            spaces=spaces,
            code=group_Data['code'],
            name=group_Data['name'],
            description=group_Data['description'],
            status=group_Data['status'],
            creation_date=group_Data['creation_date'],
            update_date=group_Data['update_date']
        )
        return self._groupsRepository.create(model_data.__dict__)

    def get(self, Groups_Id: int) -> Groups:
        return self._groupsRepository.get(Groups_Id)

    def update(self, Groups_Id: int, group_Data: dict) -> Groups:
        spaces = self._spacesRepository.get(group_Data['spaces'])
        model_data = Groups(
            spaces=spaces,
            code=group_Data['code'],
            name=group_Data['name'],
            description=group_Data['description'],
            status=group_Data['status'],
            creation_date=group_Data['creation_date'],
            update_date=group_Data['update_date']
        )
        return self._groupsRepository.update(Groups_Id, model_data.__dict__)

    def delete(self, Groups_Id: int) -> bool:
        return self._groupsRepository.delete(Groups_Id)

    def list_all(self) -> list[Groups]:
        return self._groupsRepository.list_all()

    def print_information(self, group_Data: dict) -> Groups:
        return self._groupsRepository.print_information(group_Data)