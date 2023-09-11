from django.contrib import admin

# Register your models here.
from authenticate.models import ClassRoom, User

admin.site.register([User, ClassRoom])
