from django.db import connection
from Domain.Models.response import GenericResponse
from Domain.Models.Company import Company
from Domain.Ports.Ports_store_procedures.company_port import CompanyRepositoryPort

class CompanyRepository(CompanyRepositoryPort):

    def create_company(self, company: Company) -> GenericResponse[int]:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                DECLARE @message NVARCHAR(500), @response INT;
                EXEC sp_AdminUser_Company_C
                    @name=%s, @legal_name=%s, @nit=%s, @country=%s, @location=%s,
                    @phone=%s, @email=%s, @postal_code=%s, @website=%s,
                    @contact_name=%s, @contact_phone=%s, @contact_email=%s,
                    @notes=%s, @status=%s, 
                    @message=@message OUTPUT, @response=@response OUTPUT;
                SELECT @message as message, @response as response;
                """, [
                    company.name,
                    company.legal_name,
                    company.nit,
                    company.country,
                    company.location,
                    company.phone,
                    company.email,
                    company.postal_code,
                    company.website,
                    company.contact_name,
                    company.contact_phone,
                    company.contact_email,
                    company.notes,
                    int(company.status)
                ])
                result = cursor.fetchone()
                mensaje = result[0]
                response = result[1]
                if response == 0:
                    return GenericResponse(message=mensaje, is_correct=False, value=None)
                return GenericResponse(value=response, message=mensaje, is_correct=True)
        except Exception as e:
            return GenericResponse(message=str(e), is_correct=False, value=None)