from django.shortcuts import render

from .carro import Carro

from productos.models import Product
from django.shortcuts import redirect #Redirecciones para que refleje los cambios

from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required(login_url="/autenticacion/iniciar_sesion") 
def agregar_producto(request, producto_id):
    
    carro = Carro(request)

    producto = Product.objects.get(id=producto_id)

    carro.agregar(producto=producto) 

    return redirect("Carrito") #Redirecciona a el carrito según el nombre del URL General


def eliminar_producto(request, producto_id):
    
    carro = Carro(request)

    producto = Product.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Carrito")

def restar_producto(request, producto_id):
    
    carro = Carro(request)

    producto = Product.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Carrito")

def limpiar_carro(request): #No necesita el producto_id
    
    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("Carrito")
