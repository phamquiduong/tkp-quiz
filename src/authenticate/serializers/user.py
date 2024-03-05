from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authenticate.serializers.group import GroupSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'full_name',)

    def create(self, validated_data):
        if User.objects.exists():
            return User.objects.create_user(**validated_data)
        return User.objects.create_superuser(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    group = GroupSerializer()

    class Meta:
        model = User
        fields = '__all__'
