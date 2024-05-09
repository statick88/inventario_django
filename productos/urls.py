from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]