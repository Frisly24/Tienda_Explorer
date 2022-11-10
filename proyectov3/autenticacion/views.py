from django.shortcuts import render, redirect
from django.views.generic import View

#Importación User Creation Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

#Importación login
from django.contrib.auth import login, logout, authenticate

#Importación Messages
from django.contrib import messages

#Importación Form Customizado de forms.py
from .forms import CustomUserCreationForm  

#Importación Usuarios
from usuarios.models import usuarios

#Importaciones para Perfil
from pedidos.models import LineaPedido
from pedidos.models import Pedido
from productos.models import Product

#Importaciones PDF
from autenticacion.utils import render_to_pdf

#Importación Http Response
from django.http import HttpResponse

#Importación form Contraseña
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

#Importación Usuario Bloqueo
from django.contrib.auth.models import User

#Importación Axes
from axes.utils import reset


# Create your views here.

#View Para la pagina de Registro
class VRegistro(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form":form}) #Devuleve el formulario

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        print(form)
    
        if form.is_valid(): #Si es valido
            usuario = form.save() #Se almacena en la tabla
            ncui = form.cleaned_data.get('cui')
            img = form.cleaned_data.get("profile_imagen")
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')

            usuario = authenticate(request=request, username=username, password=password) #Ingresa los datos a la Tabla de Usuarios de DJANGO

            login(request, usuario) #Inicia sesión

            nuevo_usuario = usuarios(user=request.user, username=request.user.username, fisrt_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email, cui=ncui, profile_image = img)
            #Registra en la Tabla Usuarios
            nuevo_usuario.save()


            return redirect('Home') #Regresa a la pagina principal
        else:
            pass
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request, "registro/registro.html", {"form":form})


def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def iniciar_sesion(request):

    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username") 
            password=form.cleaned_data.get("password")
            usuario = authenticate(request=request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                reset(username=username) #Libreria Axes
                return redirect('Home')
            else:
                messages.error(request,"Usuario no válido")
        else:
            messages.error(request,"Información no válida")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})

#Views perfil

def perfil(request):

    articulos_comprados = LineaPedido.objects.all() #Linea Pedido muestra los articulos comprados por el usuario
    pedidos_comprados = Pedido.objects.all()
    listado_todos_productos = Product.objects.all()
    listado_usuarios = usuarios.objects.all()

    return render(request, "perfil/perfil.html", {"articulos_comprados":articulos_comprados, "listado_todos_productos":listado_todos_productos, 'listado_usuarios': listado_usuarios, 'pedidos_comprados': pedidos_comprados})

def pedidos(request):

    articulos_comprados = LineaPedido.objects.all() #Linea Pedido muestra los articulos comprados por el usuario
    pedidos_comprados = Pedido.objects.all()
    listado_todos_productos = Product.objects.all()
    listado_usuarios = usuarios.objects.all()

    return render(request, "perfil/pedidos.html", {"articulos_comprados":articulos_comprados, "listado_todos_productos":listado_todos_productos, 'listado_usuarios': listado_usuarios, 'pedidos_comprados': pedidos_comprados})

class perfil_pdf(View):

    def get(self, request, *arg, **kwargs):
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        first_name = request.user.first_name
        last_name = request.user.last_name

        user={
            'id':user_id,
            'username': username,
            'first_name':first_name,
            'last_name': last_name,
            'email': email
        }

        print(user["username"])
        
        articulos_comprados = LineaPedido.objects.all()
        listado_todos_productos = Product.objects.all()
        pedidos_comprados = Pedido.objects.all()

        articulos_comprados2=[]
        listado_todos_productos2=[]
        for articulos_comprados in articulos_comprados:
        
            if articulos_comprados.user_id == user_id:
                articulos_comprados2.append(articulos_comprados)
                articulo = Product.objects.get(pk=articulos_comprados.producto_id)
                listado_todos_productos2.append(articulo)
        data={
            'articulos_comprados': articulos_comprados2,
            'listado_todos_productos': listado_todos_productos,
            'pedidos_comprados': pedidos_comprados,
            'user': user
        }
        pdf = render_to_pdf('perfil/perfil_pdf.html', data)
        
        return HttpResponse(pdf, content_type='application/pdf')

def lockout(request, credentials, *args, **kwargs):
    for i in User.objects.all():
    
        if i.username == credentials["username"]:
            correo_usuario = i.email

    try:
        enviar_mail(
            nombreusuario = credentials["username"],
            emailusuario = correo_usuario
        )
    except:
        print("No se ha podido enviar el correo")

    return render(request, "lockout/lockout.html")

def enviar_mail(**kwargs):

    asunto="Restablecimiento Contraseña Tienda Explorer"
    mensaje = render_to_string("emails/reset_pass.html",{

        "nombreusuario": kwargs.get("nombreusuario")

    })

    mensaje_texto=strip_tags(mensaje)
    from_email="tiendaexplorer2022@gmail.com"         #Correo desde el que se envia        
    to=kwargs.get("emailusuario")               #Correo al que se envia
    #to = "correo@gmail.com" #Corre de Pruebas

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)




