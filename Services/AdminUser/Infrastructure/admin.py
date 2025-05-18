from django.contrib import admin
from .ImportsModelsDB import *
from Domain.Models.User_Kafka import User_Kafka


admin.site.register(System_users)
admin.site.register(Company_license_detail)
admin.site.register(Company)
admin.site.register(Detail_license_type_services)
admin.site.register(Groups)
admin.site.register(License_type_services)
admin.site.register(License_type)
admin.site.register(Module)
admin.site.register(Permission_group)
admin.site.register(Permission_level)
admin.site.register(Permission_user)
admin.site.register(Permit)
admin.site.register(Services)
admin.site.register(Spaces)
admin.site.register(User_groups)
admin.site.register(User_Kafka)


