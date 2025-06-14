from rest_framework import serializers

class PermissionGroupSerializerUnique(serializers.Serializer):
    group = serializers.IntegerField()  # ID del grupo (FK)
    permission_level = serializers.IntegerField()  # ID del nivel de permiso (FK)
    permit = serializers.IntegerField()  # ID del permiso (FK)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)

