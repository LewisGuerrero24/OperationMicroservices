# API/views.py

from rest_framework.views import APIView
from API.Controller.CompanyController import CompanyController
from API.Serializer.CompanySerializer import CompanySerializer
from drf_yasg.utils import swagger_auto_schema

class CreateCompanyView(APIView):
    
    @swagger_auto_schema(request_body=CompanySerializer)
    def post(self, request):
        controller = CompanyController()
        return controller.create_company(request)
