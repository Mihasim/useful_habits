# Generated by Django 4.2.9 on 2024-01-08 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=datetime.time(9, 50, 32, 226022), verbose_name='Время'),
        ),
    ]