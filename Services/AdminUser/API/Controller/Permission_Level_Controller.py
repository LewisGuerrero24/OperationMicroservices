from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.PermissionLevel.PermissionLevelSerializer import PermissionLevelSerializer
from ..Serializer.PermissionLevel.PermissionLevelSerializerUnique import PermissionLevelSerializerUnique
from Application.Services.PermissionLevel_Services import PermissionLevel_Services
from Infrastructure.Adapters.Permission_Level_RepositoryI import PermissionLevelRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PermissionLevelListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._permission_Level_Service = PermissionLevel_Services(PermissionLevelRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los nivel de permisos",
        responses={200: PermissionLevelSerializer(many=True)}
    )
    def get(self, request):
        PermissionLevels = self._permission_Level_Service.list_all()
        serialized_PermissionLevels = PermissionLevelSerializer(PermissionLevels, many=True)
        return Response(serialized_PermissionLevels.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=PermissionLevelSerializerUnique,
        operation_description="Crea un nuevo nivel de permiso",
        responses={201: PermissionLevelSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = PermissionLevelSerializer(data=request.data)
        if serializer.is_valid():
            PermissionLevel_data = serializer.validated_data
            PermissionLevel = self._permission_Level_Service.create(PermissionLevel_data)
            return Response(PermissionLevelSerializer(PermissionLevel).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermissionLevelDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._permission_Level_Service = PermissionLevel_Services(PermissionLevelRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un nivel de permiso por ID",
        responses={200: PermissionLevelSerializer(), 404: "nivel de permiso no encontrado"}
    )
    def get(self, request, permission_level_id):
        try:
            PermissionLevel = self._permission_Level_Service.get(permission_level_id)
            return Response(PermissionLevelSerializer(PermissionLevel).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=PermissionLevelSerializerUnique,
        operation_description="Actualiza un nivel de permiso existente",
        responses={200: PermissionLevelSerializerUnique, 400: "Datos inválidos", 404: "nivel de permiso no encontrado"}
    )
    def put(self, request, permission_level_id):
        serializer = PermissionLevelSerializerUnique(data=request.data)
        if serializer.is_valid():
            PermissionLevel_data = serializer.validated_data
            try:
                PermissionLevel = self._permission_Level_Service.update(permission_level_id, PermissionLevel_data)
                return Response(PermissionLevelSerializer(PermissionLevel).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un nivel de permiso por ID",
        responses={
            204: "nivel de permiso eliminado",
            400: "No se pudo eliminar el nivel de permiso",
            404: "nivel de permiso no encontrado"
        }
    )
    def delete(self, request, permission_level_id):
        try:
            result = self._permission_Level_Service.delete(permission_level_id)
            if result:
                return Response({'message': 'nivel de permiso eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el nivel de permiso'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)