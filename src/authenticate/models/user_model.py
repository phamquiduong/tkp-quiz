from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from authenticate.models.class_room_model import ClassRoom


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        extra_fields['full_name'] = extra_fields.get('full_name', None) or email.split('@')[0]
        extra_fields['name'] = extra_fields['full_name'].split()[-1]

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_active'] = True
        extra_fields['is_superuser'] = True
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None

    email = models.EmailField(_('email address'), unique=True)

    name = models.CharField(max_length=30, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email} - {'Teacher' if self.is_superuser else 'Student'}"

    def is_teacher(self):
        return self.is_superuser

    def is_student(self):
        return not self.is_superuser