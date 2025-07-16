from rest_framework import serializers

class SystemUserSerializerLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()