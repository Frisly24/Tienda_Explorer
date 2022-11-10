"""proyectov3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls), # Es la aplicación original de admin.
    #URL General
    path('', include('core.erp.urls')),
    # URL Productos
    path('Productos/', include('productos.urls')),
    # URL para el carro
    path('carro/', include('carro.urls')),
    # URL para la autenticacion
    path('Autenticacion/', include('autenticacion.urls')),
    # URL para el pedido
    path('pedidos/', include('pedidos.urls')),
    # URL Reconocimiento
    #path('reconocimiento/', include('reconocimiento.urls')),
]



