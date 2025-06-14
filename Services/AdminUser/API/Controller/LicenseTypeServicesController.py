from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.License_type_service.License_Type_ServiceSerializer import LicenseTypeServicesSerializer
from ..Serializer.License_type_service.License_TypeServicesSerializerUnique import LicenseTypeServicesSerializerUnique
from Application.Services.LicenseTypeService_Services import LicenseTypeServiceS
from Infrastructure.Adapters.LicenseTypeServicesRepositoryI import LicenseTypeServiceRepositoryImpl
from Infrastructure.Adapters.LicenseTypeRepositoryI import LicenseTyperRepositoryImpl
from Infrastructure.Adapters.ServiceRepositoryI import ServiceRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LicenseTypeServiceListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.LicenseTypeService_Services = LicenseTypeServiceS(LicenseTypeServiceRepositoryImpl(), LicenseTyperRepositoryImpl(), ServiceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos las tipo de licencias",
        responses={200: LicenseTypeServicesSerializer(many=True)}
    )
    def get(self, request):
        license_type_servicess = self.LicenseTypeService_Services.list_all()
        serialized_license_type_servicess = LicenseTypeServicesSerializer(license_type_servicess, many=True)
        return Response(serialized_license_type_servicess.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=LicenseTypeServicesSerializerUnique,
        operation_description="Crea una nueva tipo de licencia",
        responses={201: LicenseTypeServicesSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = LicenseTypeServicesSerializer(data=request.data)
        if serializer.is_valid():
           license_type_services_data = serializer.validated_data
           license_type_services = self.LicenseTypeService_Services.create(license_type_services_data)
           return Response(LicenseTypeServicesSerializer(license_type_services).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LicenseTypeServiceDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.LicenseTypeService_Services = LicenseTypeServiceS(LicenseTypeServiceRepositoryImpl(), LicenseTyperRepositoryImpl(), ServiceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene una tipo de licencia por ID",
        responses={200: LicenseTypeServicesSerializer(), 404: "tipo de licencia no encontrada"}
    )
    def get(self, request, license_type_services_id):
        try:
            license_type_service = self.LicenseTypeService_Services.get(license_type_services_id)
            return Response(LicenseTypeServicesSerializer(license_type_service).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=LicenseTypeServicesSerializerUnique,
        operation_description="Actualiza una tipo de licencia existente",
        responses={200: LicenseTypeServicesSerializerUnique, 400: "Datos inválidos", 404: "tipo de licencia no encontrada"}
    )
    def put(self, request, license_type_services_id):
        serializer = LicenseTypeServicesSerializerUnique(data=request.data)
        if serializer.is_valid():
           license_type_services_data = serializer.validated_data
           try:
                license_type_service = self.LicenseTypeService_Services.update(license_type_services_id,license_type_services_data)
                return Response(LicenseTypeServicesSerializer(license_type_service).data, status=status.HTTP_200_OK)
           except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un tipo de licencia por ID",
        responses={
            204: "tipo de licencia eliminada",
            400: "No se pudo eliminar el usuario",
            404: "Usuario no encontrado"
        }
    )
    def delete(self, request, license_type_services_id):
        try:
            result = self.LicenseTypeService_Services.delete(license_type_services_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)