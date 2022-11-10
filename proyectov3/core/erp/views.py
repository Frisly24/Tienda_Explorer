from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from productos.models import * 

#Importar Carro
from carro.carro import Carro

#Importación Usuarios
from usuarios.models import usuarios


# Create your views here.

def Home(request):

    carro = Carro(request) #Inicia el carro, al iniciar la aplicación

    return render(request, "ProyectoWebApp/Home.html")

def Contacto(request):

    return render(request, "ProyectoWebApp/Contacto.html")

def Base(request):

    return render(request, "ProyectoWebApp/base.html")


"""
def listaproductos(request):
    data = {
        'title': 'Productos',
        'Product': Product.objects.all(),
        'link': 'listaproductos',

    }
    return render(request, "admin/lista_productos.html", data)    

"""    

class listaproductosListView(ListView):
    model = Product
    template_name ='admin/lista_productos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos'
        return context


def carrito(request):

    return render(request, "ProyectoWebApp/carrito.html")


def checkout(request):
    info_usuario = usuarios.objects.all()
    pedido_valido = True
    return render(request, "ProyectoWebApp/checkout.html", {"info_usuario":info_usuario, "pedido_valido": pedido_valido})   
    # return render(request, "ProyectoWebApp/checkout.html", {"info_usuario":info_usuario})
    