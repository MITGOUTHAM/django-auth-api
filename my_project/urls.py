from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import ensure_csrf_cookie

schema_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version="v1",
        description="Authentication API with OTP & JWT-in-cookie",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("authentication.urls")),  
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    
]
