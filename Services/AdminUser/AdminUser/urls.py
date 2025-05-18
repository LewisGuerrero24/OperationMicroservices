"""
URL configuration for AdminUser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import permissions
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 
from API.views import UserListController, UserDetailController, CompanyListController,Company_License_DetailListController, LicenseTypeListController, ServiceListController,LicenseTypeServiceListController, DetailLicenseTypeServiceListController, GroupsListController, ModuleListController, PermitListController, PermissionLevelListController, PermissionUserListController, PermissionGroupListController, UserGroupListController
from API.views import SpacesListController, SpacesDetailController, CompanyDetailController, Company_License_DetailController, LicenseTypeDetailController, ServiceDetailController, LicenseTypeServiceDetailController, DetailLicenseTypeServiceDetailController, GroupsDetailController, ModuleDetailController,  PermitDetailController, PermissionLevelDetailController, PermissionUserDetailController, PermissionGroupDetailController, UserGroupDetailController
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

def home_view(request):
    return HttpResponseRedirect('/swagger/')

@login_required
def custom_admin_dashboard(request):
    return render(request, 'custom_dashboard.html')

schema_view = get_schema_view(
   openapi.Info(
      title="Mi API",
      default_version='v1',
      description="Documentación de la API con Swagger",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('custom_dashboard/', custom_admin_dashboard, name=''),
    path('logout/', LogoutView.as_view(next_page='/custom_dashboard/'), name='logout'),
    path('admin/', admin.site.urls),
    #path('usuarios/', CreateUserView.as_view(), name='crear_usuario'),
    path('', home_view),
    path('users/', UserListController.as_view(), name='user_list'),
    path('users/<uuid:user_id>/', UserDetailController.as_view(), name='user_detail'),
    path('space/', SpacesListController.as_view(), name='space_list'),
    path('space/<int:space_id>/', SpacesDetailController.as_view(), name='space_detail'), 
    path('company/', CompanyListController.as_view(), name='company_list'),
    path('company/<int:company_id>/', CompanyDetailController.as_view(), name='company_detail'),
    path('companylicensedetail/', Company_License_DetailListController.as_view(), name='company_license_detail_list'),
    path('companylicensedetail/<int:company_license_detail_id>/', Company_License_DetailController.as_view(), name='company_license_detail'),
    path('licenseType/', LicenseTypeListController.as_view(), name='license_type_list'),
    path('licenseType/<int:type_license_id>/', LicenseTypeDetailController.as_view(), name='license_type_detail'),
    path('service/', ServiceListController.as_view(), name='service_list'),
    path('service/<int:service_id>/', ServiceDetailController.as_view(), name='service_detail'),   
    path('licenseTypeServices/', LicenseTypeServiceListController.as_view(), name='license_type_service_list'),
    path('licenseTypeServices/<int:license_type_services_id>/', LicenseTypeServiceDetailController.as_view(), name='license_type_service_detail'),
    path('detailLicenseTypeServices/', DetailLicenseTypeServiceListController.as_view(), name='detail_license_type_service_list'),
    path('detailLicenseTypeServices/<int:detail_license_type_services_id>/', DetailLicenseTypeServiceDetailController.as_view(), name='detail_license_type_service_detail'),
    path('groups/', GroupsListController.as_view(), name='groups_list'),
    path('groups/<int:groups_id>/', GroupsDetailController.as_view(), name='groups_detail'),
    path('modules/', ModuleListController.as_view(), name='modules_list'),
    path('modules/<int:module_id>/', ModuleDetailController.as_view(), name='modules_detail'),
    path('permits/', PermitListController.as_view(), name='permits_list'),
    path('permits/<int:permit_id>/', PermitDetailController.as_view(), name='permits_detail'),
    path('permissionLevels/', PermissionLevelListController.as_view(), name='permission_levels_list'),
    path('permissionLevels/<int:permission_level_id>/', PermissionLevelDetailController.as_view(), name='permission_levels_detail'),
    path('permissionUsers/', PermissionUserListController.as_view(), name='permission_users_list'),
    path('permissionUsers/<int:permission_user_id>/', PermissionUserDetailController.as_view(), name='permission_users_detail'),
    path('permissionGroups/', PermissionGroupListController.as_view(), name='permission_groups_list'),
    path('permissionGroups/<int:permission_group_id>/', PermissionGroupDetailController.as_view(), name='permission_groups_detail'),
    path('userGroups/', UserGroupListController.as_view(), name='user_groups_list'),
    path('userGroups/<int:user_group_id>/', UserGroupDetailController.as_view(), name='user_groups_detail'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]   
