from rest_framework import serializers

class PermitSerializerUnique(serializers.Serializer):
    spaces = serializers.IntegerField()  # ID del espacio (FK)
    module = serializers.IntegerField()  # ID del modulo (FK)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200, required=False, allow_null=True)
    is_custom = serializers.BooleanField(default=False)
    system_defined = serializers.BooleanField(default=False)
    logical_route = serializers.CharField(max_length=200, required=False, allow_null=True)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
