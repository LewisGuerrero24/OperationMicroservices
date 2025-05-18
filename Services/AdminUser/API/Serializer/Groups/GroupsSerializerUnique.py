from rest_framework import serializers

class GroupsSerializerUnique(serializers.Serializer):
    spaces = serializers.IntegerField()  # ID del espacio (FK)
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)