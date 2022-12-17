from django.contrib import admin
from .models.canal import Canal
from .models.invitacion import Invitacion
from .models.mensaje import Mensaje
from .models.server import Servidor
from .models.usuario import Usuario

# Register your models here.
admin.site.register(Canal)
admin.site.register(Invitacion)
admin.site.register(Mensaje)
admin.site.register(Servidor)
admin.site.register(Usuario)
