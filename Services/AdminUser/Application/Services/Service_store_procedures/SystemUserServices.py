from Application.DTOs.DTO_LoginResponse import DTO_LoginResponse
from Domain.Models.response import GenericResponse
from Domain.Ports.Ports_store_procedures.System_users_login import SystemUsersLoginPort
from Domain.Ports.Security.token_service_interface import TokenServiceInterface
from Infrastructure.Adapters.Adapters_store_procedures.System_user_repository import SystemUsersRepository
from shared.DTO_Login import DTO_Login
from ...UseCases.UseCase_store_procedures.System_user_UseCase import SystemUsersUseCasePort


class SystemUserServices(SystemUsersUseCasePort):

    def __init__(self, SystemUsers_LoginPort: SystemUsersLoginPort, token_service: TokenServiceInterface):
        self.SystemUsers_LoginPort = SystemUsers_LoginPort
        self.token_service = token_service


    def login(self, DTO_login: DTO_Login) -> GenericResponse[DTO_LoginResponse]:
        result = self.SystemUsers_LoginPort.login(DTO_login)
        if not result.is_correct:
            return result
        
        user = result.value

        access_token = self.token_service.create_access_token({
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "is_superuser": user.is_superuser,
            "id_space": user.spaces.id,
            "id_company": user.spaces.company.id
        })
        refresh_token = self.token_service.create_refresh_token({
            "user_id": user.id,
        })

        return GenericResponse(
            value=DTO_LoginResponse(
                access_token=access_token,
                refresh_token=refresh_token,
                user_data={"full_name": user.full_name}
            ).to_dict(),
            message="Login exitoso",
            is_correct=True
        )
