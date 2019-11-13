from django.contrib import admin
from .models import Canais
from .models import Frases
from .models import Habilidades

# Register your models here.

admin.site.register(Canais)
admin.site.register(Frases)
admin.site.register(Habilidades)
