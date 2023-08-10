from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Green Energy API",
        default_version="v1",
        description="API endpoints for Green Api",
        contact=openapi.Contact(email="vicente.19981@live.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/",schema_view.with_ui("redoc",cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]


admin.site.site_header = "Green Energy API Admin"

admin.site.site_title = "Green Energy API Admin Portal"

admin.site.index_title = "Welcome to Green Energy API Portal"

