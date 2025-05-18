from rest_framework import serializers

class GroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    spaces = serializers.UUIDField()  
    code = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    status = serializers.BooleanField(default=True)
    creation_date = serializers.DateTimeField(required=False)
    update_date = serializers.DateTimeField(required=False)