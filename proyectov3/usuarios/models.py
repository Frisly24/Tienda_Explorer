
from django.db import models
#Importacion del Modelo User
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class usuarios (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fisrt_name = models.CharField(max_length=150, null=False, default='Nombres', verbose_name='Nombres')
    last_name = models.CharField(max_length=150, null=False, default='Apellidos', verbose_name='Apellidos')

    username = models.CharField(max_length=150, null=False, default=user, verbose_name='Username')
    email = models.EmailField(max_length=150, default="correo@gmail.com", verbose_name='Correo')

    cui = models.CharField(max_length=13, unique=True, default="0", verbose_name='CUI')

    profile_image = models.ImageField(upload_to='User_Profile_Image', default='users_pictures/default.png', verbose_name='Imagen de Perfil')

    login_attempts = models.IntegerField(null=False, default=0, verbose_name='Login Attempts')
    active_account = models.BooleanField(null=False, default=True, verbose_name='Active Account')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'usuarios_info'
        verbose_name='Cliente'
        verbose_name_plural = 'Clientes'
        ordering=['id']





