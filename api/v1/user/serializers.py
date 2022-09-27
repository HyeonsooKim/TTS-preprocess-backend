# api.v1.user.serializers.py

# DRF
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import AuthenticationFailed
# Django
from django.contrib.auth import get_user_model
from datetime import date
# Internal
from apps.user.models import User
from .tokens import generate_token

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'name']

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(
            username=validated_data.get('username'),
            password=password,
            name=validated_data.get('name'),
        )
        user.set_password(password)
        user.save()

        return user
    
    def validate(self, data):
        id = data.get('id', None)

        if User.objects.filter(id=id).exists():
            raise serializers.ValidationError("Username already exists")

        data['date_joined'] = date.today()

        return data


class SignInSerializers(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        write_only=True,
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if not user.check_password(password):
                raise AuthenticationFailed("Wrong password")
        else:
            raise AuthenticationFailed("User account not exist")

        payload_value = user.id
        payload = {
            "subject": payload_value,
        }

        access_token = generate_token(payload, "access")
        refresh_token = generate_token(payload, "refresh")

        data = {
            'user': username,
            'refresh': refresh_token,
            'access': access_token,
        }

        return data