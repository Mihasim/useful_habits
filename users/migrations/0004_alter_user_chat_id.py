# Generated by Django 5.0 on 2024-01-08 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='chat_id'),
        ),
    ]
