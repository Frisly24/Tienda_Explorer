from django.urls import path

from .views import VRegistro, cerrar_sesion, iniciar_sesion, perfil, pedidos, perfil_pdf

#Importación para Password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    #URLS PERFIL
    path('perfil', perfil, name="perfil"),
    path('pedidos', pedidos, name="pedidos"),
    path('perfil_pdf', perfil_pdf.as_view(), name="perfil_pdf"),
    #URLS RESET PASSWORD
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_complete.html"), name="password_reset_complete"),
]




