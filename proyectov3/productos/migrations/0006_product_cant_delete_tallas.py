# Generated by Django 4.0.3 on 2022-11-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_remove_tallas_creacion_remove_tallas_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cant',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.DeleteModel(
            name='Tallas',
        ),
    ]
