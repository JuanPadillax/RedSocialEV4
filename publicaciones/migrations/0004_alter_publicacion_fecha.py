# Generated by Django 5.1.1 on 2024-12-19 16:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_alter_publicacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
