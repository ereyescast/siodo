# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 06:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idestado', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tipo_estado', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField(blank=True, null=True)),
                ('documento_identidad', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idservicio', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(blank=True, max_length=45, null=True)),
                ('tipservicio', models.CharField(blank=True, max_length=45, null=True)),
                ('duracion', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
