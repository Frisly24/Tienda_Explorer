# Generated by Django 4.0.3 on 2022-11-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_product_cant_delete_tallas'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product/img2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/img1'),
        ),
    ]