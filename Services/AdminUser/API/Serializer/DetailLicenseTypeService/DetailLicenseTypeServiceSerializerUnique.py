from rest_framework import serializers

class DetailLicenseTypeServicesSerializerUnique(serializers.Serializer):
    license_type_services = serializers.IntegerField()  # ID del License_type_services (FK)
    company_license_detail = serializers.IntegerField()  # ID del Company_license_detail (FK)
    allowed_limit = serializers.IntegerField()
    used_limit = serializers.IntegerField(default=0)
    unit = serializers.CharField(max_length=50, default='registros')
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
