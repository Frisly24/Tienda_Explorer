from django.shortcuts import render

#Importación Login
from django.contrib.auth.decorators import login_required

#Importación models
from pedidos.models import LineaPedido, Pedido

#Importación carro
from carro.carro import Carro

#Importación Messages
from django.contrib import messages

#Importación Redirect
from django.shortcuts import redirect

#Importación render to string
from django.template.loader import render_to_string

#Importación Strip Tags
from django.utils.html import strip_tags

#Importación mail django
from django.core.mail import send_mail

#Importación productos (verificación de inventario)
from productos.models import Product

#Importación Usuarios 
from usuarios.models import usuarios


# Create your views here.

@login_required(login_url="/autenticacion/iniciar_sesion")

def procesar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido = pedido
        ))

    #Verificacion de Pedido Valido.
    pedido_valido = True            #Verificación valides.

    lineas_pedido2=lineas_pedido
    lineas_pedido3=lineas_pedido
    lineas_pedido4=lineas_pedido

    
    #Ciclo For Lineas_pedido2 / Verifica que si haya la cantidad de articulos Solicitados.

    for lineas_pedido2 in lineas_pedido2:   #Confimarcion que el pedido sea valido
        en_stock = Product.objects.get(pk=lineas_pedido2.producto_id)
        nueva_cantidad = en_stock.cant - lineas_pedido2.cantidad  #En stock hace referencia a la tabla de productos y lineas al dato almacenado        
        
        if nueva_cantidad<0:
            pedido_valido = False
            break
        else:
            pedido_valido = True


    #Guarda la nueva cantidad al terminar la verificación
    if pedido_valido:
            for lineas_pedido3 in lineas_pedido3:   #Almacenamiento del pedido valido
                en_stock = Product.objects.get(pk=lineas_pedido3.producto_id)
                nueva_cantidad = en_stock.cant - lineas_pedido3.cantidad        
                en_stock.cant=nueva_cantidad


                en_stock.save()

            LineaPedido.objects.bulk_create(lineas_pedido)
            #Solicita la información del usuario
            info_usuario = usuarios.objects.all()

            enviar_mail(
                pedido = pedido,
                lineas_pedido = lineas_pedido4,
                nombreusuario = request.user.username,
                emailusuario = request.user.email
            )
            
            #Limpieza carrito
            carro = Carro(request)
            carro.limpiar_carro() #Limpia el Carrito
            

            return redirect("pedidos") #Regresa a los pedidos
            
    else: 
        info_usuario = usuarios.objects.all()
        return render(request, "ProyectoWebApp/checkout.html", {"info_usuario":info_usuario, "pedido_valido": pedido_valido})
    
#Funcion Mail

def enviar_mail(pedido, lineas_pedido, nombreusuario, emailusuario, **kwargs):

    asunto = "Comprobante de pedido"
    mensaje = render_to_string("emails/pedido.html",{

        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "nombreusuario": nombreusuario,

        })

    mensaje_texto=strip_tags(mensaje)
    from_email="tiendaexplorer2022@gmail.com" #Correo desde donde se envia
    to=emailusuario       #Se puede obtener directo de la base de datos o obtenerlo del formulario
    #to = "frislygcornejo@gmail.com" #De momento se deja así porque allí es donde necesito enviarlo

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)


