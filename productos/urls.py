from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductoViewSet

from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    # URLs de vistas normales
    path('', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),

    # URLs de la API
    path('api/', include(router.urls)),

    # Documentación de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]