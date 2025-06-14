from rest_framework.response import Response
from rest_framework import status
from Application.Services.CompanyServices import CreateCompanyUseCase
from Infrastructure.Adapters.Adapters_store_procedures.company_repository import CompanyRepository
from ..Serializer.CompanySerializerSP import CompanySerializerSP
from ..Serializer.serializer_to_dto import serializer_to_dto
from Application.DTOs.CompanyDTO import CompanyDTO

class CompanyController:
    def __init__(self):
        self.use_case = CreateCompanyUseCase(CompanyRepository())

    def create_company(self, request):
        serializer = CompanySerializerSP(data=request.data)
        if serializer.is_valid():
            dto: CompanyDTO = serializer_to_dto(serializer, CompanyDTO)
            response = self.use_case.create_company(dto)
            if response.is_correct:
                return Response({"message": response.message, "es_correcto": response.is_correct, "Valor": response.value}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": response.message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)