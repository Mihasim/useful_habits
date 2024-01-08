from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=False, verbose_name="Пользователь активен")
    telegram_id = models.CharField(max_length=50, verbose_name='telegram_id', null=False, blank=False, unique=True)
    chat_id = models.CharField(max_length=50, verbose_name='chat_id', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return (f'{self.email}')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
