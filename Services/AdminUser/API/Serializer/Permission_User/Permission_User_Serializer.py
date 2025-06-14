from rest_framework import serializers

class PermissionUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    system_user = serializers.UUIDField()  # Suponiendo que el ID de System_users es un entero
    permission_level = serializers.UUIDField()
    permit = serializers.UUIDField()
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
