from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Company.CompanySerializer import CompanySerializer
from ..Serializer.Company.CompanySerializerUnique import CompanySerializerUnique
from Application.Services.CompanyService import CompanyService
from Infrastructure.Adapters.CompanyRepositoryI import CompanyRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CompanyListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._company_service = CompanyService(CompanyRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos las compañias",
        responses={200: CompanySerializer(many=True)}
    )
    def get(self, request):
        users = self._company_service.list_all()
        serialized_users = CompanySerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=CompanySerializerUnique,
        operation_description="Crea una nueva compañia",
        responses={201: CompanySerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            user = self._company_service.create(company_data)
            return Response(CompanySerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._company_service = CompanyService(CompanyRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene una compañia por ID",
        responses={200: CompanySerializer(), 404: "COmpañia no encontrada"}
    )
    def get(self, request, company_id):
        try:
            user = self._company_service.get(company_id)
            return Response(CompanySerializer(user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=CompanySerializerUnique,
        operation_description="Actualiza una compañia existente",
        responses={200: CompanySerializerUnique, 400: "Datos inválidos", 404: "Compañia no encontrada"}
    )
    def put(self, request, company_id):
        serializer = CompanySerializerUnique(data=request.data)
        if serializer.is_valid():
            company_data = serializer.validated_data
            try:
                user = self._company_service.update(company_id, company_data)
                return Response(CompanySerializer(user).data, status=status.HTTP_200_OK)
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
    def delete(self, request, company_id):
        try:
            result = self._company_service.delete(company_id)
            if result:
                return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)