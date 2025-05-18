from rest_framework import serializers

class PermitSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    spaces = serializers.UUIDField()  # ID del espacio
    module = serializers.UUIDField()  # ID del modulo
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200, required=False, allow_null=True)
    is_custom = serializers.BooleanField(default=False)
    system_defined = serializers.BooleanField(default=False)
    logical_route = serializers.CharField(max_length=200, required=False, allow_null=True)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
