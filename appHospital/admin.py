
from django.contrib import admin
# Register your models here.
from .models.familiar import tbl_familiar
from .models.historia import tbl_historia
from .models.paciente import tbl_paciente
from .models.persona import tbl_persona
from .models.rol import tbl_rol
from .models.signovital import tbl_signovital

admin.site.register(tbl_persona)
admin.site.register(tbl_familiar)


