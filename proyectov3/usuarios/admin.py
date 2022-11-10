from django.contrib import admin
from .models import usuarios

# Register your models here.


class UsuariosAdmin(admin.ModelAdmin):
    fields=('user','fisrt_name', 'last_name', 'username', 'cui', 'email', 'login_attempts') #Campos a mostrar
    readonly_fields=('user','fisrt_name', 'last_name', 'username', 'cui', 'email', 'login_attempts') #Evitar la modificacion en la edicion de registro
    list_display = ['last_name', 'fisrt_name', 'username', 'email', 'cui', 'login_attempts','active_account' ] #Propiedades visibles del campo
    ordering = ['last_name']    #Ordena registros por
    search_fields = ['fisrt_name','last_name', 'username', 'cui'] #Busqueda según estos elementos
    list_per_page=15    #Cantidad de items por pagina
    

admin.site.register(usuarios, UsuariosAdmin)
