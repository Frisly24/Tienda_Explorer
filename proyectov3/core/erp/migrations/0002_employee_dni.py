# Generated by Django 4.0.3 on 2022-10-04 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dni',
            field=models.CharField(default=0, max_length=150, unique=True, verbose_name='Dni'),
        ),
    ]
