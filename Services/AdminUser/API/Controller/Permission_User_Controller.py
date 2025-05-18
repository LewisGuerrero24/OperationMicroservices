from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Permission_User.Permission_User_Serializer import PermissionUserSerializer
from ..Serializer.Permission_User.Permission_User_SerializerUnique import PermissionUserSerializerUnique
from Application.Services.PermissionUser_Services import PermissionUser_Services
from Infrastructure.Adapters.Permission_User_RepositoryI import PermissionUserRepositoryImpl
from Infrastructure.Adapters.UserRepositoryI import UserRepositoryImpl
from Infrastructure.Adapters.Permission_Level_RepositoryI import PermissionLevelRepositoryImpl
from Infrastructure.Adapters.PermitRepositoryI import PermitRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PermissionUserListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._permission_User_Service = PermissionUser_Services(PermissionUserRepositoryImpl(), UserRepositoryImpl(), PermissionLevelRepositoryImpl(), PermitRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los permisos",
        responses={200: PermissionUserSerializer(many=True)}
    )
    def get(self, request):
        PermissionUsers = self._permission_User_Service.list_all()
        serialized_PermissionUsers = PermissionUserSerializer(PermissionUsers, many=True)
        return Response(serialized_PermissionUsers.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=PermissionUserSerializerUnique,
        operation_description="Crea un nuevo permiso",
        responses={201: PermissionUserSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = PermissionUserSerializer(data=request.data)
        if serializer.is_valid():
            PermissionUser_data = serializer.validated_data
            PermissionUser = self._permission_User_Service.create(PermissionUser_data)
            return Response(PermissionUserSerializer(PermissionUser).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermissionUserDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._permission_User_Service = PermissionUser_Services(PermissionUserRepositoryImpl(), UserRepositoryImpl(), PermissionLevelRepositoryImpl(), PermitRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un permiso por ID",
        responses={200: PermissionUserSerializer(), 404: "permiso no encontrado"}
    )
    def get(self, request, permission_user_id):
        try:
            PermissionUser = self._permission_User_Service.get(permission_user_id)
            return Response(PermissionUserSerializer(PermissionUser).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=PermissionUserSerializerUnique,
        operation_description="Actualiza un permiso existente",
        responses={200: PermissionUserSerializerUnique, 400: "Datos inválidos", 404: "permiso no encontrado"}
    )
    def put(self, request, permission_user_id):
        serializer = PermissionUserSerializerUnique(data=request.data)
        if serializer.is_valid():
            PermissionUser_data = serializer.validated_data
            try:
                PermissionUser = self._permission_User_Service.update(permission_user_id, PermissionUser_data)
                return Response(PermissionUserSerializer(PermissionUser).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un permiso por ID",
        responses={
            204: "permiso eliminado",
            400: "No se pudo eliminar el permiso",
            404: "permiso no encontrado"
        }
    )
    def delete(self, request, permission_user_id):
        try:
            result = self._permission_User_Service.delete(permission_user_id)
            if result:
                return Response({'message': 'permiso eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el permiso'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:            
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)