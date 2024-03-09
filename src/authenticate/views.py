from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authenticate.models import Group
from authenticate.permissions.user import IsTeacher
from authenticate.serializers.group import GroupSerializer
from authenticate.serializers.user import RegisterSerializer, UserSerializer

User = get_user_model()


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)


class GroupsListAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.filter(is_teacher=False)
    serializer_class = GroupSerializer
    permission_classes = [IsTeacher]


class GroupsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.filter(is_teacher=False)
    serializer_class = GroupSerializer
    permission_classes = [IsTeacher]
