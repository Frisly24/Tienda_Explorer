from django.urls import path
from core.erp import views
from core.erp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
     
    path('Contacto/', views.Contacto, name="Contacto"), #Eliminar
    path('Base/', views.Base, name="Base"), # Me permite acceder a la plantilla base
    
    path('Listaproductos/', listaproductosListView.as_view() , name="listaproductos"),

    path('Carrito', views.carrito, name="Carrito"),

    path('Checkout', views.checkout, name="Checkout"),

   
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
