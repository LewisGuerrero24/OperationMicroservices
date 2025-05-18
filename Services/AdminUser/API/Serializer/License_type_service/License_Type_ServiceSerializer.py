from rest_framework import serializers

class LicenseTypeServicesSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    license_type = serializers.UUIDField()  # ID de License_type
    service = serializers.UUIDField()     # ID de Services
    max_records = serializers.IntegerField()
    duration_days = serializers.IntegerField()
    custom_limit_note = serializers.CharField(max_length=255, required=False, allow_null=True)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
