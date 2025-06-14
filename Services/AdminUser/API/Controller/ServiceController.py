from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Service.ServiceSerializer import ServicesSerializer
from ..Serializer.Service.ServiceSerializerUnique import ServicesSerializerUnique
from Application.Services.Services_service import Services_Services
from Infrastructure.Adapters.ServiceRepositoryI import ServiceRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ServiceListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service_Service = Services_Services(ServiceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos las servicios",
        responses={200: ServicesSerializer(many=True)}
    )
    def get(self, request):
        users = self._service_Service.list_all()
        serialized_users = ServicesSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ServicesSerializerUnique,
        operation_description="Crea una nueva servicio",
        responses={201: ServicesSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = ServicesSerializerUnique(data=request.data)
        if serializer.is_valid():
            service_data = serializer.validated_data
            user = self._service_Service.create(service_data)
            return Response(ServicesSerializerUnique(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service_Service = Services_Services(ServiceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene una servicio por ID",
        responses={200: ServicesSerializer(), 404: "servicio no encontrada"}
    )
    def get(self, request, service_id):
        try:
            user = self._service_Service.get(service_id)
            return Response(ServicesSerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ServicesSerializerUnique,
        operation_description="Actualiza una servicio existente",
        responses={200: ServicesSerializerUnique, 400: "Datos inválidos", 404: "servicio no encontrada"}
    )
    def put(self, request, service_id):
        serializer = ServicesSerializerUnique(data=request.data)
        if serializer.is_valid():
            service_data = serializer.validated_data
            try:
                user = self._service_Service.update(service_id, service_data)
                return Response(ServicesSerializer(user).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un servicio por ID",
        responses={
            204: "servicio eliminada",
            400: "No se pudo eliminar el servicio",
            404: "servicio no encontrado"
        }
    )
    def delete(self, request, service_id):
        try:
            result = self._service_Service.delete(service_id)
            if result:
                return Response({'message': 'servicio eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el servicio'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)