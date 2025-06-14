from rest_framework import serializers

class PermissionUserSerializerUnique(serializers.Serializer):
    system_user = serializers.UUIDField()  # Suponiendo que el ID de System_users es un entero
    permission_level = serializers.IntegerField()
    permit = serializers.IntegerField()
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
