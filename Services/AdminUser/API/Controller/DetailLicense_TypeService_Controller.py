from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..Serializer.DetailLicenseTypeService.DetailLicenseTypeServiceSerializer import DetailLicenseTypeServicesSerializer
from ..Serializer.DetailLicenseTypeService.DetailLicenseTypeServiceSerializerUnique import DetailLicenseTypeServicesSerializerUnique
from Application.Services.Detail_License_TypeS import Detail_LicenseTypeS
from Infrastructure.Adapters.DetailLicense_TypeServicesRepositoryI import DetailLicenseTypeServiceRepositoryImpl
from Infrastructure.Adapters.LicenseTypeServicesRepositoryI import LicenseTypeServiceRepositoryImpl
from Infrastructure.Adapters.CompanyLicenseDetailI import CompanyLicenseDetailRepositoryImpl

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DetailLicenseTypeServiceListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._DetailLicenseTypeServices = Detail_LicenseTypeS(DetailLicenseTypeServiceRepositoryImpl(), CompanyLicenseDetailRepositoryImpl(), LicenseTypeServiceRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos las tipo de licencias",
        responses={200: DetailLicenseTypeServicesSerializer(many=True)}
    )
    def get(self, request):
        users = self._DetailLicenseTypeServices.list_all()
        serialized_users = DetailLicenseTypeServicesSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=DetailLicenseTypeServicesSerializerUnique,
        operation_description="Crea una nueva tipo de licencia",
        responses={201: DetailLicenseTypeServicesSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = DetailLicenseTypeServicesSerializer(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            user = self._DetailLicenseTypeServices.create(company_data)
            return Response(DetailLicenseTypeServicesSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailLicenseTypeServiceDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._DetailLicenseTypeServices = Detail_LicenseTypeS(DetailLicenseTypeServiceRepositoryImpl(), CompanyLicenseDetailRepositoryImpl(), LicenseTypeServiceRepositoryImpl())


    @swagger_auto_schema(
        operation_description="Obtiene una tipo de licencia por ID",
        responses={200: DetailLicenseTypeServicesSerializer(), 404: "tipo de licencia no encontrada"}
    )
    def get(self, request, detail_license_type_services_id):
        try:
            user = self._DetailLicenseTypeServices.get(detail_license_type_services_id)
            return Response(DetailLicenseTypeServicesSerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=DetailLicenseTypeServicesSerializerUnique,
        operation_description="Actualiza una tipo de licencia existente",
        responses={200: DetailLicenseTypeServicesSerializerUnique, 400: "Datos inválidos", 404: "tipo de licencia no encontrada"}
    )
    def put(self, request, detail_license_type_services_id):
        serializer = DetailLicenseTypeServicesSerializerUnique(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            try:
                user = self._DetailLicenseTypeServices.update(detail_license_type_services_id, company_data)
                return Response(DetailLicenseTypeServicesSerializer(user).data, status=status.HTTP_200_OK)
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
    def delete(self, request, detail_license_type_services_id):
        try:
            result = self._DetailLicenseTypeServices.delete(detail_license_type_services_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)