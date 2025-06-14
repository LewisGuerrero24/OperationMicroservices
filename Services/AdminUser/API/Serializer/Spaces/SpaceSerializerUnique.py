from rest_framework import serializers
import uuid

class SpacesSerializerUnique(serializers.Serializer):
    company = serializers.IntegerField(required=True)
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)