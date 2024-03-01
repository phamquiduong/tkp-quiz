from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):  # pylint: disable=W0223
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField(write_only=True)

        self.fields['access'] = serializers.CharField(read_only=True)
        self.fields['refresh'] = serializers.CharField(read_only=True)
