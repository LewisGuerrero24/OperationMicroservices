from rest_framework.views import APIView
from API.Controller.CompanySPController import CompanyController
from API.Serializer.CompanySerializerSP import CompanySerializerSP
from drf_yasg.utils import swagger_auto_schema

class CreateCompanyView(APIView):
    
    @swagger_auto_schema(request_body=CompanySerializerSP)
    def post(self, request):
        controller = CompanyController()
        return controller.create_company(request)

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

