# Generated by Django 5.0 on 2024-07-02 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_instrutor_codigoinstrutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigoinstrutor',
            name='instrutor',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.instrutor', verbose_name='instrutor'),
        ),
    ]
