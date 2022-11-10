from django.urls import path
from productos import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Tienda, name="Tienda"), #Permite ver la lista de productos
    #Al tener '' simplemente se ingresa con la URL productos referenciada en urls.py de core.erp

    #views.Tienda hace referencia al HTML
    #name = "Tienda" sirve para poder hacer referencia en otra parte
    path('Producto/<int:id>', views.Producto, name="Producto"), # Permite ver individualmente el HTML de un producto en especifico
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

