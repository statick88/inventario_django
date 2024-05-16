from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from productos.views import ProductoViewSet

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Crear un ernrutador y registrar la vista de ProductoViewSet
router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API de Productos",
      default_version='v1',
      description="Documentación de la API de Productos",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
