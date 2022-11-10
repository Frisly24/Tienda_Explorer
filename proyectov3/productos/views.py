from django.shortcuts import render

from productos.models import Product
# Create your views here.

def Tienda(request):

    productos=Product.objects.all()


    return render(request, "productos/Tienda.html", {"productos":productos})

def Producto(request, id):

    prod = Product.objects.get(pk=id)

    return render(request, "productos/CompraProducto.html",  {"prod":prod})    

