# Generated by Django 5.0 on 2024-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='telegram_id'),
        ),
    ]