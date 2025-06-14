from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.LicenseType.LIcenseTypeSerializer import LicenseTypeSerializer
from ..Serializer.LicenseType.LicenseTypeSerializerUnique import LicenseTypeSerializerUnique
from Application.Services.License_Type_Service import LicenseType_Service
from Infrastructure.Adapters.LicenseTypeRepositoryI import LicenseTyperRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LicenseTypeListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._licenseType_Service = LicenseType_Service(LicenseTyperRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos las tipo de licencias",
        responses={200: LicenseTypeSerializer(many=True)}
    )
    def get(self, request):
        users = self._licenseType_Service.list_all()
        serialized_users = LicenseTypeSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=LicenseTypeSerializerUnique,
        operation_description="Crea una nueva tipo de licencia",
        responses={201: LicenseTypeSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = LicenseTypeSerializer(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            user = self._licenseType_Service.create(company_data)
            return Response(LicenseTypeSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LicenseTypeDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._licenseType_Service = LicenseType_Service(LicenseTyperRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene una tipo de licencia por ID",
        responses={200: LicenseTypeSerializer(), 404: "tipo de licencia no encontrada"}
    )
    def get(self, request, type_license_id):
        try:
            user = self._licenseType_Service.get(type_license_id)
            return Response(LicenseTypeSerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=LicenseTypeSerializerUnique,
        operation_description="Actualiza una tipo de licencia existente",
        responses={200: LicenseTypeSerializerUnique, 400: "Datos inválidos", 404: "tipo de licencia no encontrada"}
    )
    def put(self, request, type_license_id):
        serializer = LicenseTypeSerializerUnique(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            try:
                user = self._licenseType_Service.update(type_license_id, company_data)
                return Response(LicenseTypeSerializer(user).data, status=status.HTTP_200_OK)
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
    def delete(self, request, type_license_id):
        try:
            result = self._licenseType_Service.delete(type_license_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)