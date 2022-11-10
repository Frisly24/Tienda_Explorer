from django.db import models

#Importación User
from django.contrib.auth import get_user_model

#Importacion producto
from productos.models import Product

#Importación Función F, sum y Float
from django.db.models import F, Sum, FloatField

# Create your models here.
User = get_user_model()

class Pedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE) #Elimina en Casada en relación al Usuario
    entregado = models.BooleanField(default=False)
    operacion = models.CharField(max_length=50, null=False, default='compra')
    created_at = models.DateTimeField(auto_now_add=True) 
    
    
    def __str__(self):
        return self.operacion 
        #return self.id

    @property
    def total(self):
        pass
        return self.lineapedido_set.agregate(
            
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name='pedido'
        verbose_name_plural = 'pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    #Extra.
    operacion = models.CharField(max_length=50, null=False, default='compra')
    entregado = models.BooleanField(default=False)

    
    

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    def __str__(self):
        return self.operacion

    class Meta:
        db_table = 'lineapedidos'
        verbose_name='Linea pedido' #Linea Pedido
        verbose_name_plural = 'Lineas pedidos' #Linea Pedidos
        ordering=['id']