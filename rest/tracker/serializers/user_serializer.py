from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from tracker.models import User


class UserCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'avatarPath', 'dateJoined', 'lastLogin', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }
        read_only_fields = ['dateJoined', 'lastLogin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')

        if request and request.method in ['GET']:
            self.fields.pop('password', None)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'avatarPath']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):  # noqa
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return {'user': user}
        raise serializers.ValidationError('Incorrect Credentials')
