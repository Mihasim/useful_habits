from datetime import datetime

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    periodicity_daily = 'daily'
    periodicity_every_two_days = 'every_two_days'
    periodicity_every_three_days = 'every_three_days'
    periodicity_every_four_days = 'every_four_days'
    periodicity_every_five_days = 'every_five_days'
    periodicity_every_six_days = 'every_six_days'
    periodicity_once_a_week = 'once_a_week'
    periodicity = [
        (periodicity_daily, 'ежедневно'),
        (periodicity_every_two_days, 'каждые два дня'),
        (periodicity_every_three_days, 'каждые три дня'),
        (periodicity_every_four_days, 'каждые четыре дня'),
        (periodicity_every_five_days, 'каждые пять дней'),
        (periodicity_every_six_days, 'каждые шесть дней'),
        (periodicity_once_a_week, 'раз в неделю'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(default=datetime.now().time(), verbose_name='Время')
    action = models.TextField(verbose_name='Действие')
    sign_of_a_pleasant_habit = models.BooleanField(verbose_name='Признак приятной привычки', default=False)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    periodicity = models.CharField(max_length=20, verbose_name='Периодичность',  choices=periodicity) #  Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    award = models.TextField(verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение')
    sign_of_publicity = models.BooleanField(verbose_name="Признак публичности", default=False)

    def __str__(self):
        return f'{self.user}, {self.place}, {self.action}, {self.periodicity}, {self.time_to_complete}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
