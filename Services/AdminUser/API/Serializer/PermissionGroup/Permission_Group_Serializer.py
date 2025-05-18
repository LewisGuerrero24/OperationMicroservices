from rest_framework import serializers

class PermissionGroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    group = serializers.UUIDField()  # ID del grupo (FK)
    permission_level = serializers.UUIDField()  # ID del nivel de permiso (FK)
    permit = serializers.UUIDField()  # ID del permiso (FK)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
