
from django.contrib import admin
# Register your models here.
from .models.persona import personaModel
from .models.rol import rolModel


admin.site.register(personaModel)



