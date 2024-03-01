from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authenticate.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'email', 'full_name']


class RegisterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    full_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'full_name',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
