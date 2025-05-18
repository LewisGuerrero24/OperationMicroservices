from Domain.Ports.GroupsRepository import GroupsRepository
from Domain.Models.Groups import Groups 
from Infrastructure.ModelsBD.Groups import Groups as Groupsbd
from Infrastructure.Mappers.GroupsMapper import GroupsMapper



class GroupsRepositoryImpl(GroupsRepository):
    def create(self, Groups_data: dict) -> Groups:
        model = Groupsbd.objects.create(**Groups_data)
        return GroupsMapper.to_domain(model)

    def get(self, Groups_id: int) -> Groups:
        model = Groupsbd.objects.get(id=Groups_id)
        return model

    def update(self, Groups_id: int, Groups_data: dict) -> Groups:
        model = Groupsbd.objects.get(id=Groups_id)
        for key, value in Groups_data.items():
            setattr(model, key, value)
        model.save()
        return GroupsMapper.to_domain(model)

    def delete(self, Groups_id:int) -> bool:
        model = Groupsbd.objects.get(id=Groups_id)
        model.delete()
        return True

    def list_all(self) -> list[Groups]:
        Groups = Groupsbd.objects.all()
        return [GroupsMapper.to_domain(u) for u in Groups]

    def print_information(self, Groups_data: dict) -> Groups:
        return Groupsbd(**Groups_data)  