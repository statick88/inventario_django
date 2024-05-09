from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages 

productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        
        producto_nuevo = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        producto_nuevo.save()

        messages.success(request, 'Producto agregado exitosamente.')

        return redirect('listar_productos')

    return render(request, 'agregar.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def actualizar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        cantidad = request.POST.get("cantidad")
        for producto in productos:
            if producto.nombre == nombre:
                producto.precio = precio
                producto.cantidad = cantidad
                break
        return redirect("productos:listar_productos")
    else:
        producto_id = request.GET.get('id')
        producto = Producto.objects.get(pk=producto_id)
        return render(request, "actualizar.html", {'producto': producto})


def eliminar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        for producto in productos:
            if producto.nombre == nombre:
                productos.remove(producto)
                break
        return redirect("listar_productos")
    return render(request, "eliminar.html")

def buscar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        for producto in productos:
            if producto.nombre == nombre:
                return render(request, "buscar.html", {"producto": producto})
        return render(request, "buscar.html", {"producto": None})
    return render(request, "buscar.html")