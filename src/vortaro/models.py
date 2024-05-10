# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anlam(models.Model):
    anlam_id = models.AutoField(primary_key=True)
    anlam_sira = models.IntegerField()
    anlam = models.TextField()
    fiil = models.IntegerField()
    gos = models.IntegerField()
    madde = models.ForeignKey('Madde', models.DO_NOTHING)
    tipkes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anlam'


class AnlamOzellik(models.Model):
    anlam = models.ForeignKey(Anlam, models.DO_NOTHING)
    ozellik = models.ForeignKey('Ozellik', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'anlam_ozellik'


class Atasozu(models.Model):
    madde = models.OneToOneField('Madde', models.DO_NOTHING, primary_key=True)
    madde_0 = models.TextField(db_column='madde')  # Field renamed because of name conflict.
    on_taki = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atasozu'


class Madde(models.Model):
    madde_id = models.AutoField(primary_key=True)
    anlam_gor = models.IntegerField()
    anlam_say = models.IntegerField()
    birlesikler = models.TextField(blank=True, null=True)
    cesit_say = models.IntegerField()
    cesit = models.IntegerField()
    cogul_mu = models.IntegerField()
    egik_mi = models.IntegerField()
    font = models.TextField(blank=True, null=True)
    gosterim_tarihi = models.TextField(blank=True, null=True)
    kac = models.IntegerField()
    kelime_no = models.IntegerField()
    lisan_kodu = models.IntegerField()
    lisan = models.TextField(blank=True, null=True)
    madde_duz = models.TextField()
    madde = models.TextField()
    on_taki = models.TextField(blank=True, null=True)
    ozel_mi = models.IntegerField()
    taki = models.TextField(blank=True, null=True)
    telaffuz = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'madde'


class MaddeAtasozu(models.Model):
    madde = models.ForeignKey(Madde, models.DO_NOTHING)
    atasozu_madde = models.ForeignKey(Atasozu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'madde_atasozu'


class Ornek(models.Model):
    ornek_id = models.AutoField(primary_key=True)
    anlam = models.ForeignKey(Anlam, models.DO_NOTHING)
    kac = models.IntegerField()
    ornek_sira = models.IntegerField()
    ornek = models.TextField(blank=True, null=True)
    yazar = models.ForeignKey('Yazar', models.DO_NOTHING, blank=True, null=True)
    yazar_vd = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ornek'


class Ozellik(models.Model):
    ozellik_id = models.AutoField(primary_key=True)
    ekno = models.IntegerField()
    kisa_adi = models.TextField()
    tam_adi = models.TextField()
    tur = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ozellik'


class Yazar(models.Model):
    yazar_id = models.AutoField(primary_key=True)
    ekno = models.IntegerField()
    kisa_adi = models.TextField()
    tam_adi = models.TextField()

    class Meta:
        managed = False
        db_table = 'yazar'
