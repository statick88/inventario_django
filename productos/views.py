from django.shortcuts import render, redirect
from .models import Producto

productos = []

def listar_productos(request):
    return render(request, "listar.html", {"productos": productos})

def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        cantidad = request.POST.get("cantidad")
        productos.append(Producto(nombre, precio, cantidad))
        return redirect("listar_productos")
    return render(request, "agregar.html")

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
        return redirect("listar_productos")
    return render(request, "actualizar.html")

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