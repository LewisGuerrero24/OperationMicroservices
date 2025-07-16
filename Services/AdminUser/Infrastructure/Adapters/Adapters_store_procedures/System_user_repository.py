import hashlib
from django.db import connection
from Domain.Models.Company import Company
from Domain.Models.Spaces import  Spaces
from Domain.Models.response import GenericResponse
from Domain.Models.System_User import SystemUsers
from Domain.Ports.Ports_store_procedures.System_users_login import SystemUsersLoginPort
from shared.DTO_Login import DTO_Login

def hash_password_sha256(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

class SystemUsersRepository(SystemUsersLoginPort):

    def login(self, dtoLogin: DTO_Login) -> GenericResponse[SystemUsers]:
        try:
            password_hashed = hash_password_sha256(dtoLogin.password)
            with connection.cursor() as cursor:
                cursor.execute("""
                    DECLARE @message NVARCHAR(500), @response BIT;
                    EXEC sp_AdminUser_Login
                        @Username=%s, @PassWordHash=%s, 
                        @message=@message OUTPUT, @response=@response OUTPUT;
                    SELECT @message as message, @response as response;
                    """,
                    [
                        dtoLogin.username,
                        dtoLogin.password  # Usa el password encriptado correctamente
                    ])

                # ✅ PRIMER result set: Puede ser datos del usuario o nada
                user_row = None
                first_result = cursor.fetchall()

                if len(first_result) == 1 and len(first_result[0]) == 2:
                    # Caso: SOLO SELECT @message, @response (error)
                    message = first_result[0][0]
                    response = first_result[0][1]
                    if not response:
                        return GenericResponse(message=message, is_correct=False, value=None)
                else:
                    # Caso: Tenemos datos del usuario
                    user_row = first_result[0]
                    cursor.nextset()  # Mover al siguiente result set: SELECT @message, @response
                    message_result = cursor.fetchall()
                    message = message_result[0][0]
                    response = message_result[0][1]

                    if not response:
                        return GenericResponse(message=message, is_correct=False, value=None)

                if user_row is None:
                    return GenericResponse(message="No se pudo recuperar el usuario.", is_correct=False, value=None)

                print("User_row: ", user_row)
                print("Response: ", response)
                print("Message: ", message)

                #✅ Construir usuario normalmente
                user = SystemUsers(
                    id=user_row[0],
                    full_name=user_row[1],
                    username=user_row[2],
                    email=user_row[3],
                    is_superuser=user_row[4],
                    last_login=user_row[5],
                    status=user_row[6],
                    password=user_row[7],
                    spaces=Spaces(
                        id=user_row[8],
                        code=user_row[9],
                        name=user_row[10],
                        description=user_row[11],
                        status=user_row[12],
                        company=Company(
                            id=user_row[13],
                            name=user_row[14],
                            legal_name=user_row[15],
                            nit=user_row[16],
                            country=user_row[17],
                            location=user_row[18],
                            phone=user_row[19],
                            email=user_row[20],
                            postal_code=user_row[21],
                            website=user_row[22],
                            contact_name=user_row[23],
                            contact_phone=user_row[24],
                            contact_email=user_row[25],
                            notes=user_row[26],
                            status=user_row[27]
                        )
                    )
                )

                return GenericResponse(value=user, message=message, is_correct=True)

        except Exception as e:
            return GenericResponse(message=str(e), is_correct=False, value=None)

