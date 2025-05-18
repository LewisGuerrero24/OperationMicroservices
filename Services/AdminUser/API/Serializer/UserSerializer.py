from rest_framework import serializers
import uuid
class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    spaces = serializers.UUIDField()
    full_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=256, write_only=True)
    is_superuser = serializers.BooleanField(default=False)
    last_login = serializers.DateTimeField(required=False)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)

    # def validate_id(self, value):
    #     try:
    #         UUID(value, version=4)
    #     except ValueError:
    #         raise serializers.ValidationError("El valor de 'id' no es un UUID válido.")
    #     return value
