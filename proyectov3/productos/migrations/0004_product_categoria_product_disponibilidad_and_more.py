# Generated by Django 4.0.3 on 2022-11-01 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_product_talla'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Niños', 'Niños')], default='Hombre', max_length=15, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='product',
            name='disponibilidad',
            field=models.BooleanField(default='True', verbose_name='Disponibilidad'),
        ),
        migrations.AddField(
            model_name='tallas',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tallas',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Actualización'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Negro', 'Negro'), ('Gris', 'Gris'), ('Blanco', 'Blanco'), ('Rojo', 'Rojo'), ('Azul Marino', 'Azul Marino'), ('Marino', 'Marino'), ('Azul', 'Azul'), ('Ocean', 'Ocean'), ('Gris', 'Gris')], default='Negro', max_length=15, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio'),
        ),
    ]
