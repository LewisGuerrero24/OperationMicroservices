from rest_framework import serializers

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField()
    legal_name = serializers.CharField(required=False, allow_null=True)
    nit = serializers.CharField()
    country = serializers.CharField()
    location = serializers.CharField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()
    postal_code = serializers.CharField(required=False, allow_null=True)
    website = serializers.CharField(required=False, allow_null=True)
    contact_name = serializers.CharField(required=False, allow_null=True)
    contact_phone = serializers.CharField(required=False, allow_null=True)
    contact_email = serializers.EmailField(required=False, allow_null=True)
    notes = serializers.CharField(required=False, allow_null=True)
    status = serializers.BooleanField()