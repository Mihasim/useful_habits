from datetime import timedelta

from rest_framework.exceptions import ValidationError


def habit_validator(habit):
    """
    -Исключить одновременный выбор связанной привычки и указания вознаграждения.
    -У приятной привычки не может быть вознаграждения или связанной привычки.
    """
    try:
        if habit['sign_of_a_pleasant_habit']:
            if habit['related_habit'] or habit['award']:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')

        if habit['related_habit'] is not None and habit['award'] is not None:
            raise ValidationError('Невозможен одновременный выбор связанной привычки и указания вознаграждения.')
    except KeyError:
        pass


def habit_time_validator(habit):
    """
    -Время выполнения должно быть не больше 120 секунд.
    """
    try:
        if habit['time_to_complete'] > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд.')
    except KeyError:
        pass


def related_habit_validator(habit):
    """
    -В связанные привычки могут попадать только привычки с признаком приятной привычки.

    """
    try:
        if not habit['related_habit'].sign_of_a_pleasant_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')
    except KeyError:
        pass
