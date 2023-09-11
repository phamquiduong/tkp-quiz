import os

from authenticate.models import User


def create_superuser():
    email = os.getenv('SUPER_ADMIN_EMAIL')
    password = os.getenv('SUPER_ADMIN_PASSWORD')
    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(email=email, password=password)
