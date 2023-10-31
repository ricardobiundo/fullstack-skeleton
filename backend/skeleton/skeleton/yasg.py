from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


def get_schema():
    schema_view = get_schema_view(
        openapi.Info(
            title="Skeleton",
            default_version="v1",
            description="API endpoints for Skeleton",
            terms_of_service="",
            contact=openapi.Contact(email="skeleton@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    return schema_view
