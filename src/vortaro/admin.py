from django.contrib import admin

from vortaro.models import Madde, Anlam, Ozellik, AnlamOzellik, Ornek, Yazar, Atasozu, MaddeAtasozu

# Register your models here.


admin.site.register(Madde)
admin.site.register(Anlam)
admin.site.register(Ozellik)
admin.site.register(AnlamOzellik)
admin.site.register(Ornek)
admin.site.register(Yazar)
admin.site.register(Atasozu)
admin.site.register(MaddeAtasozu)
