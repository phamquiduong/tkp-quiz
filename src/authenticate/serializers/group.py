from rest_framework import serializers

from authenticate.models import Group


class GroupSerializer(serializers.ModelSerializer):
    is_teacher = serializers.CharField(read_only=True)

    class Meta:
        model = Group
        fields = '__all__'
