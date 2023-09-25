from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/tkp-web/img/favicon.ico', permanent=True)),
    path('admin/', admin.site.urls),
    path('', include('authenticate.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
