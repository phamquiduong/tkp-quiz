from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    title = models.CharField(max_length=255, unique=True)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        db_table = 'groups'


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_active'] = True
        extra_fields['is_superuser'] = True
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    username = None

    email = models.EmailField(_('email address'), unique=True)

    full_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'
