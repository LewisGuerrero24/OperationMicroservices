
from rest_framework import serializers

class ServicesSerializerUnique(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    codeService = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
