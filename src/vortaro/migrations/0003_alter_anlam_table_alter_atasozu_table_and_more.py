# Generated by Django 4.2.13 on 2024-05-10 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vortaro', '0002_anlamozellik_maddeatasozu_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='anlam',
            table='anlam',
        ),
        migrations.AlterModelTable(
            name='atasozu',
            table='atasozu',
        ),
        migrations.AlterModelTable(
            name='madde',
            table='madde',
        ),
        migrations.AlterModelTable(
            name='ornek',
            table='ornek',
        ),
        migrations.AlterModelTable(
            name='ozellik',
            table='ozellik',
        ),
        migrations.AlterModelTable(
            name='yazar',
            table='yazar',
        ),
    ]