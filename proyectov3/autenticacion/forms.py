from django import forms  

#Importación User
from django.contrib.auth.models import User  

#Importación Creación de Usuario
from django.contrib.auth.forms import UserCreationForm

#Importación Verificación Correo  
from django.core.exceptions import ValidationError  

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password1']
    
    cui = forms.IntegerField(label='CUI', help_text='Código Único de Identificación CUI')
    profile_imagen = forms.ImageField(label='Foto de perfil')

    def email_clean(self):
        
        email = self.cleaned_data.get('email')
        new = User.objects.filter(email = email)  
        if new.count():  
            raise ValidationError("El email ya esta vinculado con otra cuenta, utiliza uno diferente.")  
        return email 
