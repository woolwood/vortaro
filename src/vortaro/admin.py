from django.contrib import admin

from vortaro.models import Madde, Anlam, Ozellik, Anlam_ozellik, Ornek, Yazar, Atasozu, Madde_atasozu

# Register your models here.


admin.site.register(Madde)
admin.site.register(Anlam)
admin.site.register(Ozellik)
admin.site.register(Anlam_ozellik)
admin.site.register(Ornek)
admin.site.register(Yazar)
admin.site.register(Atasozu)
admin.site.register(Madde_atasozu)
