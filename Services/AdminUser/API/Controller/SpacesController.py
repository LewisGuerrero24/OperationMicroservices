from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Spaces.SpaceSerializer import SpacesSerializer
from ..Serializer.Spaces.SpaceSerializerUnique import SpacesSerializerUnique
from Application.Services.Spaces_Services import Spaces_Services
from Infrastructure.Adapters.CompanyRepositoryI import CompanyRepositoryImpl
from Infrastructure.Adapters.SpaceRepositoryI import SpaceRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SpacesListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._space_service = Spaces_Services(SpaceRepositoryImpl(), CompanyRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los usuarios",
        responses={200: SpacesSerializer(many=True)}
    )
    def get(self, request):
        users = self._space_service.list_all()
        serialized_users = SpacesSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=SpacesSerializerUnique,
        operation_description="Crea un nuevo usuario",
        responses={201: SpacesSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = SpacesSerializer(data=request.data)
        if serializer.is_valid():
            space_data = serializer.validated_data
            user = self._space_service.create(space_data)
            return Response(SpacesSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpacesDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._space_service = Spaces_Services(SpaceRepositoryImpl(),CompanyRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un usuario por ID",
        responses={200: SpacesSerializer(), 404: "Usuario no encontrado"}
    )
    def get(self, request, space_id):
        try:
            user = self._space_service.get(space_id)
            return Response(SpacesSerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=SpacesSerializerUnique,
        operation_description="Actualiza un usuario existente",
        responses={200: SpacesSerializerUnique, 400: "Datos inválidos", 404: "Usuario no encontrado"}
    )
    def put(self, request, space_id):
        serializer = SpacesSerializerUnique(data=request.data)
        if serializer.is_valid():
            space_data = serializer.validated_data
            try:
                user = self._space_service.update(space_id, space_data)
                return Response(SpacesSerializer(user).data, status=status.HTTP_200_OK)
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
    def delete(self, request, space_id):
        try:
            result = self._space_service.delete(space_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)