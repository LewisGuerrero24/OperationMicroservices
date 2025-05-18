from rest_framework import serializers

class LicenseTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=200, required=False, allow_null=True)
    description = serializers.CharField(max_length=200, required=False, allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    support_level = serializers.CharField(max_length=50)
    duration_days = serializers.IntegerField()
    max_users = serializers.IntegerField()
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
