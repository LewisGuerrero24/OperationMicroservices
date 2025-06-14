from rest_framework import serializers

class UserGroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    system_user = serializers.UUIDField()  # ID del usuario del sistema (FK)
    group = serializers.UUIDField()        # ID del grupo (FK)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)