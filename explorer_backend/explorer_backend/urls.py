from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from scanner.views import home, orgs_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orgs', orgs_view),
    path('', home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
