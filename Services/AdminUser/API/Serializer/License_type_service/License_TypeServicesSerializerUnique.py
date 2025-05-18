from rest_framework import serializers

class LicenseTypeServicesSerializerUnique(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    license_type = serializers.IntegerField()  
    service = serializers.IntegerField()       
    max_records = serializers.IntegerField()
    duration_days = serializers.IntegerField()
    custom_limit_note = serializers.CharField(max_length=255, required=False, allow_null=True)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)