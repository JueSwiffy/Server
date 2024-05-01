"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions
from drf_yasg import openapi
# obtain_auth_token 추가
from rest_framework.authtoken.views import obtain_auth_token

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    """
    # CLASS : BothHttpAndHttpsSchemaGenerator
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 11:41 AM
    # DESCRIPTION
        - HTTP and HTTPS
        - https://stackoverflow.com/questions/55568431/how-can-i-configure-https-schemes-with-the-drf-yasg-auto-generated-swagger-pag
    """

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

schema_url_v1_patterns = [
    # Login
    path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="Swiffy Server API",
        default_version='v1',
        description="Swiffy Server API Description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,  # HTTP and HTTPS
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_v1_patterns
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),  # Include default auth URLs
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Auto DRF API docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    # Login & Logout
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
