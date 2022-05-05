from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.hashers import make_password

class RegistrationDataSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128,write_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)

    def validate(self, data):
        data = super().validate(data)
        if data.get('email'):
            if CustomUser.objects.filter(email=data.get('email')).exists():
                raise serializers.ValidationError("This email already registered!")
        return data

    def create(self,validated_data):
        instance = CustomUser.objects.create(**validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class AuthorizationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()

    def validate(self, data):
        data = super().validate(data)
        if not (data.get('email') or data.get('username')):
            raise serializers.ValidationError("Send email or username to sign in")
        return data



class NameAndIdSerializer(serializers.Serializer):

    name = serializers.CharField()
    id = serializers.IntegerField()