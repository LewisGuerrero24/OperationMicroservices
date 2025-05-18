from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.CompanyLicenseDetail.CompanyLicenseDetailSerializer import CompanyLicenseDetailSerializer
from ..Serializer.CompanyLicenseDetail.CompanyLicenseDetailUniqueSerilizer import CompanyLicenseDetailSerializerUnique
from Application.Services.CompanyLicenseDetailService import Company_License_DetailService
from Infrastructure.Adapters.CompanyLicenseDetailI import CompanyLicenseDetailRepositoryImpl
from Infrastructure.Adapters.CompanyRepositoryI import CompanyRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class Company_License_DetailListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._CompanyDetailService = Company_License_DetailService(CompanyLicenseDetailRepositoryImpl(), CompanyRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos las compañias",
        responses={200: CompanyLicenseDetailSerializer(many=True)}
    )
    def get(self, request):
        users = self._CompanyDetailService.list_all()
        serialized_users = CompanyLicenseDetailSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=CompanyLicenseDetailSerializerUnique,
        operation_description="Crea una nueva compañia",
        responses={201: CompanyLicenseDetailSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = CompanyLicenseDetailSerializer(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            user = self._CompanyDetailService.create(company_data)
            return Response(CompanyLicenseDetailSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Company_License_DetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._CompanyDetailService = Company_License_DetailService(CompanyLicenseDetailRepositoryImpl(),CompanyRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene una compañia por ID",
        responses={200: CompanyLicenseDetailSerializer(), 404: "COmpañia no encontrada"}
    )
    def get(self, request, company_license_detail_id):
        try:
            user = self._CompanyDetailService.get(company_license_detail_id)
            return Response(CompanyLicenseDetailSerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=CompanyLicenseDetailSerializerUnique,
        operation_description="Actualiza una compañia existente",
        responses={200: CompanyLicenseDetailSerializerUnique, 400: "Datos inválidos", 404: "Compañia no encontrada"}
    )
    def put(self, request, company_license_detail_id):
        serializer = CompanyLicenseDetailSerializerUnique(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            try:
                user = self._CompanyDetailService.update(company_license_detail_id, company_data)
                return Response(CompanyLicenseDetailSerializer(user).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un compañia por ID",
        responses={
            204: "Compañia eliminada",
            400: "No se pudo eliminar el usuario",
            404: "Usuario no encontrado"
        }
    )
    def delete(self, request, company_license_detail_id):
        try:
            result = self._CompanyDetailService.delete(company_license_detail_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)