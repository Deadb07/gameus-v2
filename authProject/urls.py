
from django.contrib import admin
from django.urls import path

from authApp.views.usuario.usuarioViewSet import UsuarioViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/list', UsuarioViewSet.as_view({'get':'list'})),
]
