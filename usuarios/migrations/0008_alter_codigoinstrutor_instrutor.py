# Generated by Django 5.0 on 2024-07-02 23:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_codigoinstrutor_instrutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigoinstrutor',
            name='instrutor',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.instrutor', verbose_name='instrutor'),
        ),
    ]
