from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_validator, habit_time_validator, related_habit_validator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {'related_habit': {'required': False}, 'user': {'required': False}}  # Сделать поле необязательным для заполнения
        validators = [
            habit_validator, habit_time_validator, related_habit_validator
        ]
