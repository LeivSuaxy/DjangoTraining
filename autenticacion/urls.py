from django.urls import path

from .views import VRegistro, cerrar_sesion, logear

urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),
    path('cerrar/', cerrar_sesion, name='cerrar'),
    path('login/', logear, name='logear'),
]
