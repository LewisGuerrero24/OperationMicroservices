from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.UserSerializer import UserSerializer
from ..Serializer.UserSerializerUnique import UserSerializerUnique
from Application.Services.UserService import UserService
from Infrastructure.Adapters.UserRepositoryI import UserRepositoryImpl
from Infrastructure.Adapters.SpaceRepositoryI import SpaceRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService(UserRepositoryImpl(), SpaceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los usuarios",
        responses={200: UserSerializer(many=True)}
    )
    def get(self, request):
        users = self.user_service.list_all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=UserSerializerUnique,
        operation_description="Crea un nuevo usuario",
        responses={201: UserSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = self.user_service.create(user_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService(UserRepositoryImpl(), SpaceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un usuario por ID",
        responses={200: UserSerializer(), 404: "Usuario no encontrado"}
    )
    def get(self, request, user_id):
        try:
            user = self.user_service.get(user_id)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


    

    @swagger_auto_schema(
        request_body=UserSerializerUnique,
        operation_description="Actualiza un usuario existente",
        responses={200: UserSerializerUnique, 400: "Datos inválidos", 404: "Usuario no encontrado"}
    )
    def put(self, request, user_id):
        serializer = UserSerializerUnique(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            try:
                user = self.user_service.update(user_id, user_data)
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un usuario por ID",
        responses={
            204: "Usuario eliminado",
            400: "No se pudo eliminar el usuario",
            404: "Usuario no encontrado"
        }
    )
    def delete(self, request, user_id):
        try:
            result = self.user_service.delete(user_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)