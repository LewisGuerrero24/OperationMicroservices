from rest_framework import serializers
import uuid

class CompanyLicenseDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    company = serializers.UUIDField()  # Suponiendo que el ID de Company es un UUID
    overage_allowed = serializers.BooleanField(default=False)
    overage_cost = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    start_date = serializers.DateField()
    cost = serializers.DecimalField(max_digits=20, decimal_places=6, required=False, allow_null=True)
    end_date = serializers.DateField(required=False, allow_null=True)
    payment_reference = serializers.CharField(max_length=100, required=False, allow_null=True)
    auto_renew = serializers.BooleanField(default=False)
    observations = serializers.CharField(max_length=200, required=False, allow_null=True)
    user_limit = serializers.IntegerField()
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
