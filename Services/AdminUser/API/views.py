from rest_framework.views import APIView
from API.Controller.CompanySPController import CompanyController
from API.Serializer.CompanySerializerSP import CompanySerializerSP
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from API.Serializer.serializer_store_procedures.System_user_serializer import SystemUserSerializerLogin
from API.Controller.StoreProcedureController.SystemUserController import SystemUserController

class CreateCompanyView(APIView):
    
    @swagger_auto_schema(request_body=CompanySerializerSP)
    def post(self, request):
        controller = CompanyController()
        return controller.create_company(request)
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('id', openapi.IN_PATH, description="ID de la empresa", type=openapi.TYPE_INTEGER)
    ])
    def delete(self, request, id):
        controller = CompanyController()
        return controller.delete_company(request, id)

class SystemUserView(APIView):
    @swagger_auto_schema(request_body=SystemUserSerializerLogin)
    def post(self, request):
        controller = SystemUserController()
        return controller.login(request)

from .Controller.UserController import UserListController, UserDetailController
from .Controller.SpacesController import SpacesListController, SpacesDetailController
from .Controller.CompanyController import CompanyListController, CompanyDetailController
from .Controller.Company_LicenseDetailController import Company_License_DetailListController, Company_License_DetailController
from .Controller.LicenseTypeControllers import LicenseTypeListController, LicenseTypeDetailController
from .Controller.ServiceController import ServiceListController, ServiceDetailController
from .Controller.LicenseTypeServicesController import LicenseTypeServiceListController, LicenseTypeServiceDetailController
from .Controller.DetailLicense_TypeService_Controller import DetailLicenseTypeServiceListController, DetailLicenseTypeServiceDetailController
from .Controller.GroupsController import GroupsListController, GroupsDetailController
from .Controller.ModuleController import ModuleListController, ModuleDetailController
from .Controller.PermitController import PermitListController, PermitDetailController
from .Controller.Permission_Level_Controller import PermissionLevelListController, PermissionLevelDetailController
from .Controller.Permission_User_Controller import PermissionUserListController, PermissionUserDetailController
from .Controller.Permission_Group_Controller import PermissionGroupListController, PermissionGroupDetailController
from .Controller.User_Group_Controller import UserGroupListController, UserGroupDetailController

