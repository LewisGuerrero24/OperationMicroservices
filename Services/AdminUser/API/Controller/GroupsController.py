from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Groups.GroupsSerializer import GroupsSerializer
from ..Serializer.Groups.GroupsSerializerUnique import GroupsSerializerUnique
from Application.Services.GroupsService import Groups_Service
from Infrastructure.Adapters.GroupRepositoryI import GroupsRepositoryImpl
from Infrastructure.Adapters.SpaceRepositoryI import SpaceRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class GroupsListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._groups_Service = Groups_Service(GroupsRepositoryImpl(), SpaceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los grupos",
        responses={200: GroupsSerializer(many=True)}
    )
    def get(self, request):
        groups = self._groups_Service.list_all()
        serialized_groups = GroupsSerializer(groups, many=True)
        return Response(serialized_groups.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=GroupsSerializerUnique,
        operation_description="Crea un nuevo grupo",
        responses={201: GroupsSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = GroupsSerializer(data=request.data)
        if serializer.is_valid():
            space_data = serializer.validated_data
            group = self._groups_Service.create(space_data)
            return Response(GroupsSerializer(group).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupsDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._groups_Service = Groups_Service(GroupsRepositoryImpl(), SpaceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un grupo por ID",
        responses={200: GroupsSerializer(), 404: "grupo no encontrado"}
    )
    def get(self, request, groups_id):
        try:
            group = self._groups_Service.get(groups_id)
            return Response(GroupsSerializer(group).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=GroupsSerializerUnique,
        operation_description="Actualiza un grupo existente",
        responses={200: GroupsSerializerUnique, 400: "Datos inválidos", 404: "grupo no encontrado"}
    )
    def put(self, request, groups_id):
        serializer = GroupsSerializerUnique(data=request.data)
        if serializer.is_valid():
            groups_data = serializer.validated_data
            try:
                group = self._groups_Service.update(groups_id, groups_data)
                return Response(GroupsSerializer(group).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un grupo por ID",
        responses={
            204: "grupo eliminado",
            400: "No se pudo eliminar el grupo",
            404: "grupo no encontrado"
        }
    )
    def delete(self, request, groups_id):
        try:
            result = self._groups_Service.delete(groups_id)
            if result:
                return Response({'message': 'grupo eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el grupo'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)