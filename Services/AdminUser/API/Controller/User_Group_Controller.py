from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.User_Groups.User_Groups_Serializer import UserGroupsSerializer
from ..Serializer.User_Groups.User_Groups_SerializerUnique import UserGroupsSerializerUnique
from Application.Services.user_groups_service import UserGroups_Service
from Infrastructure.Adapters.User_Group_RepositoryI import UserGroupRepositoryImpl
from Infrastructure.Adapters.UserRepositoryI import UserRepositoryImpl
from Infrastructure.Adapters.GroupRepositoryI import GroupsRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserGroupListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._user_Groups_Service = UserGroups_Service(UserGroupRepositoryImpl(), UserRepositoryImpl(), GroupsRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los grupos",
        responses={200: UserGroupsSerializer(many=True)}
    )
    def get(self, request):
        UserGroups = self._user_Groups_Service.list_all()
        serialized_UserGroups = UserGroupsSerializer(UserGroups, many=True)
        return Response(serialized_UserGroups.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=UserGroupsSerializerUnique,
        operation_description="Crea un nuevo grupo",
        responses={201: UserGroupsSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = UserGroupsSerializer(data=request.data)
        if serializer.is_valid():
            UserGroups_data = serializer.validated_data
            UserGroups = self._user_Groups_Service.create(UserGroups_data)
            return Response(UserGroupsSerializer(UserGroups).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGroupDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._user_Groups_Service = UserGroups_Service(UserGroupRepositoryImpl(), UserRepositoryImpl(), GroupsRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un grupo por ID",
        responses={200: UserGroupsSerializer(), 404: "grupo no encontrado"}
    )
    def get(self, request, user_group_id):
        try:
            UserGroups = self._user_Groups_Service.get(user_group_id)
            return Response(UserGroupsSerializer(UserGroups).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=UserGroupsSerializerUnique,
        operation_description="Actualiza un grupo existente",
        responses={200: UserGroupsSerializerUnique, 400: "Datos inválidos", 404: "grupo no encontrado"}
    )
    def put(self, request, user_group_id):
        serializer = UserGroupsSerializerUnique(data=request.data)
        if serializer.is_valid():
            UserGroups_data = serializer.validated_data
            try:
                UserGroups = self._user_Groups_Service.update(user_group_id, UserGroups_data)
                return Response(UserGroupsSerializer(UserGroups).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un grupo por ID",
        responses={
            204: "grupo eliminado",
            400: "No se pudo eliminar el grupo",
            404: "Grupo no encontrado"
        }
    )
    def delete(self, request, user_group_id):
        try:
            result = self._user_Groups_Service.delete(user_group_id)
            if result:
                return Response({'message': 'grupo eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el grupo'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)            