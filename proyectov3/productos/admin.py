from django.contrib import admin

from productos.models import Product

#Importaciones
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.




"""
class ProductosAdmin(admin.ModelAdmin):
    list_display = ("name","color","pvp", "cant",)
    search_fields = ("name","color")
    list_filter = ("color",)

class SaleAdmin(admin.ModelAdmin):
    list_display = ("cli","total")
    list_filter=("date_joined",)   
    date_hierarchy="date_joined"
"""

class serviciosresource(resources.ModelResource):
    fields =('id', 'name', 'categoria', 'pvp', 'cant')
    
    class Meta:
        model = Product

@admin.register(Product)
class ServiciosAdmin(ImportExportModelAdmin):
    resource_class = serviciosresource
    #readonly_fields=('creacion', 'update')
    list_display = ['name', 'color', 'categoria', 'pvp', 'cant', 'disponibilidad'] #Propiedades visibles del campo
    list_filter=['categoria', 'disponibilidad']  #Añadir buscar por filtro
    list_per_page=15    #Cantidad de items por pagina
    list_editable=['disponibilidad',]


#admin.site.register(Product, ProductosAdmin)

#admin.site.register(Sale, SaleAdmin)
#admin.site.register(DetSale)


