from django.db import models

# Create your models here.


class Madde(models.Model):
    anlam_gor = models.IntegerField(null=False)
    anlam_say = models.IntegerField(null=False)
    birlesikler = models.TextField()
    cesit_say = models.IntegerField(null=False)
    cesit = models.TextField(null=False)
    cogul_mu = models.IntegerField(null=False)
    egik_mi = models.IntegerField(null=False)
    font = models.TextField()
    gosterim_tarihi = models.IntegerField(null=False)
    kac = models.IntegerField(null=False)
    kelime_no = models.IntegerField(null=False)
    lisan_kodu = models.IntegerField(null=False)
    lisan = models.TextField()
    madde_duz = models.TextField(null=False)
    madde = models.TextField(null=False)
    on_taki = models.TextField()
    ozel_mi = models.IntegerField(null=False)
    taki = models.TextField()
    telaffuz = models.TextField()


class Anlam(models.Model):
    madde_id = models.ForeignKey(Madde, on_delete=models.CASCADE)
    anlam_sira = models.IntegerField(null=False)
    anlam = models.TextField(null=False)
    fiil = models.IntegerField(null=False)
    gos = models.IntegerField(null=False)
    tipkes = models.IntegerField(null=False)


class Ozellik(models.Model):
    ekno = models.IntegerField(null=False)
    kisa_adi = models.TextField(null=False)
    tam_adi = models.TextField(null=False)
    tur = models.IntegerField(null=False)


class Anlam_ozellik(models.Model):
    anlam_id = models.ForeignKey(Anlam, on_delete=models.CASCADE)
    ozellik_id = models.ForeignKey(Ozellik, on_delete=models.CASCADE)


class Yazar(models.Model):
    ekno = models.IntegerField(null=False)
    kisa_adi = models.TextField(null=False)
    tam_adi = models.TextField(null=False)

class Ornek(models.Model):
    anlam_id = models.ForeignKey(Anlam, on_delete=models.CASCADE)
    kac = models.IntegerField(null=False)
    ornek_sira = models.IntegerField(null=False)
    ornek = models.TextField()
    yazar_id = models.ForeignKey(Yazar, on_delete=models.CASCADE)
    yazar_vd = models.TextField()


class Atasozu(models.Model):
    madde_id = models.ForeignKey(Madde, on_delete=models.CASCADE)
    madde = models.TextField(null=False)
    on_taki = models.TextField()


class Madde_atasozu(models.Model):
    madde_id = models.ForeignKey(Madde, on_delete=models.CASCADE)
    atasozu_madde_id = models.ForeignKey(Atasozu, on_delete=models.CASCADE)


