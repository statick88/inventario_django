from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.urls import reverse 

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

        # Agregamos el mensaje de éxito
        messages.success(request, 'Producto agregado exitosamente.')

        return redirect('listar_productos')

    return render(request, 'agregar.html')

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        
        # Actualiza los campos del producto
        producto.nombre = nombre
        producto.precio = precio
        producto.cantidad = cantidad
        producto.save()
        
        return redirect('productos:listar_productos')
    else:
        return render(request, 'actualizar.html', {'producto': producto})

def eliminar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        try:
            producto = Producto.objects.get(nombre=nombre)
            producto.delete()
        except Producto.DoesNotExist:
            pass
        
        return redirect('productos:listar_productos')
    return render(request, "eliminar.html")

def buscar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        try:
            producto = Producto.objects.get(nombre=nombre)
            return render(request, "buscar.html", {"producto": producto})
        except Producto.DoesNotExist:
            return render(request, "buscar.html", {"producto": None})
    return render(request, "buscar.html")