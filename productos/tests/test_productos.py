import pytest
from productos.models import Producto

@pytest.mark.django_db
def test_crear_producto():
    producto = Producto.objects.create(
        nombre="Producto de prueba",
        precio=10.00,
        cantidad=5
    )
    assert producto.nombre == "Producto de prueba"
    assert producto.precio == 10.00
    assert producto.cantidad == 5

@pytest.mark.django_db
def test_str_producto():
    producto = Producto.objects.create(
        nombre="Producto de prueba",
        precio=10.00,
        cantidad=5
    )
    assert str(producto) == "Producto de prueba"


