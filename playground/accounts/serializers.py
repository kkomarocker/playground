from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import os


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        if validated_data['email'] == os.environ.get('HAEMAIL') \
                or validated_data['email'] == os.environ.get('HJEMAIL'):
            user = User.objects.create_superuser(
                validated_data['username'],
                validated_data['email'],
                validated_data['password'])
        else:
            user = User.objects.create_user(
                validated_data['username'],
                validated_data['email'],
                validated_data['password'])

        return user
