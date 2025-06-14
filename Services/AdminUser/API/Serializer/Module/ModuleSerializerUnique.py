from rest_framework import serializers

class ModuleSerializerUnique(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200, required=False, allow_null=True)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
