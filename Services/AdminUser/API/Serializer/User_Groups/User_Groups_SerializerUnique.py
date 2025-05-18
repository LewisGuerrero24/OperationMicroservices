from rest_framework import serializers

class UserGroupsSerializerUnique(serializers.Serializer):
    system_user = serializers.UUIDField()  # ID del usuario del sistema (FK)
    group = serializers.IntegerField()        # ID del grupo (FK)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)
