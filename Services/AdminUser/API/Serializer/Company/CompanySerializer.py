from rest_framework import serializers

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    legal_name = serializers.CharField(max_length=250, required=False, allow_null=True)
    nit = serializers.CharField(max_length=40)
    country = serializers.CharField(max_length=20)
    location = serializers.CharField(max_length=200)
    phone = serializers.IntegerField()
    email = serializers.CharField(max_length=200)
    postal_code = serializers.CharField(max_length=20, required=False, allow_null=True)
    website = serializers.CharField(max_length=100, required=False, allow_null=True)
    contact_name = serializers.CharField(max_length=100, required=False, allow_null=True)
    contact_phone = serializers.CharField(max_length=20, required=False, allow_null=True)
    contact_email = serializers.CharField(max_length=200, required=False, allow_null=True)
    notes = serializers.CharField(max_length=200, required=False, allow_null=True)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
