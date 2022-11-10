from django.db import models
from datetime import datetime


from productos.choices import color_choices, state_choices, category_choices

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Producto', unique=True)
    color = models.CharField(max_length=15, choices=color_choices, default='Negro', verbose_name='Color')
    categoria = models.CharField(max_length=15, choices=category_choices, default='Hombre', verbose_name='Categoria')
    image = models.ImageField(upload_to='product/img1', null=True, blank=True)
    image2 = models.ImageField(upload_to='product/img2', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,verbose_name='Precio')
    cant = models.IntegerField(default=0, verbose_name='Cantidad')
    disponibilidad = models.BooleanField(verbose_name='Disponibilidad', default='True')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

#Pendientes de Organización (Referencia Pedidos)
"""
class Sale(models.Model):
    #cli = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de la Venta')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='IVA')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Venta')
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    cant = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Total')
    estado = models.CharField(max_length=15, choices=state_choices, default='En Bodega', verbose_name='Estado')

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
"""