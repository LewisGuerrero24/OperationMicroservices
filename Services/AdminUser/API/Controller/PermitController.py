from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Permit.PermitSerializer import PermitSerializer
from ..Serializer.Permit.PermitSerializerUnique import PermitSerializerUnique
from Application.Services.Permit_Service import Permit_Services
from Infrastructure.Adapters.PermitRepositoryI import PermitRepositoryImpl
from Infrastructure.Adapters.SpaceRepositoryI import SpaceRepositoryImpl
from Infrastructure.Adapters.ModuleRepositoryI import ModuleRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PermitListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._permit_service = Permit_Services(PermitRepositoryImpl(), SpaceRepositoryImpl(), ModuleRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los permisos",
        responses={200: PermitSerializer(many=True)}
    )
    def get(self, request):
        permits = self._permit_service.list_all()
        serialized_permits = PermitSerializer(permits, many=True)
        return Response(serialized_permits.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=PermitSerializerUnique,
        operation_description="Crea un nuevo permiso",
        responses={201: PermitSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = PermitSerializer(data=request.data)
        if serializer.is_valid():
            permit_data = serializer.validated_data
            permit = self._permit_service.create(permit_data)
            return Response(PermitSerializer(permit).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermitDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._permit_service = Permit_Services(PermitRepositoryImpl(), SpaceRepositoryImpl(), ModuleRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un permiso por ID",
        responses={200: PermitSerializer(), 404: "permiso no encontrado"}
    )
    def get(self, request, permit_id):
        try:
            permit = self._permit_service.get(permit_id)
            return Response(PermitSerializer(permit).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=PermitSerializerUnique,
        operation_description="Actualiza un permiso existente",
        responses={200: PermitSerializerUnique, 400: "Datos inválidos", 404: "permiso no encontrado"}
    )
    def put(self, request, permit_id):
        serializer = PermitSerializerUnique(data=request.data)
        if serializer.is_valid():
            permit_data = serializer.validated_data
            try:
                permit = self._permit_service.update(permit_id, permit_data)
                return Response(PermitSerializer(permit).data, status=status.HTTP_200_OK)
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
    def delete(self, request, permit_id):
        try:
            result = self._permit_service.delete(permit_id)
            if result:
                return Response({'message': 'permiso eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el permiso'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)            