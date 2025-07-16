from API.Serializer.serializer_to_dto import serializer_to_dto
from Application.Services.Service_store_procedures.SystemUserServices import SystemUserServices
from Infrastructure.Adapters.Adapters_store_procedures.System_user_repository import SystemUsersRepository
from Infrastructure.Adapters.Security.jwt_services import JwtServices
from shared.DTO_Login import DTO_Login
from ...Serializer.serializer_store_procedures.System_user_serializer import SystemUserSerializerLogin
from rest_framework import status
from rest_framework.response import Response

class SystemUserController:
    def __init__(self):
        self.use_case = SystemUserServices(SystemUsersRepository(), JwtServices())

    def login(self, request):
        serializer = SystemUserSerializerLogin(data=request.data)
        if serializer.is_valid():
            dto: DTO_Login = serializer_to_dto(serializer, DTO_Login)
            response = self.use_case.login(dto)
            if response.is_correct:
                return Response({"message": response.message, "es_correcto": response.is_correct, "Valor": response.value}, status=status.HTTP_200_OK)
            else:
                return Response({"error": response.message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)