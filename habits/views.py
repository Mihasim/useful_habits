from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    контроллер создания привычки
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        purchased_habit = serializer.save()
        purchased_habit.user = self.request.user
        purchased_habit.save()
        print(Habit.objects.filter(pk=serializer.save().pk))


class HabitListAPIView(generics.ListAPIView):
    """
    контроллер вывода списка привычек пользователя
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPaginator  # Пагинация вывод 5 привычек на страницу

    def get_queryset(self):
        """
        Вывод привычек текущего пользователя
        """
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class PublicHabitListAPIView(generics.ListAPIView):
    """
    контроллер вывода списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPaginator  # Пагинация вывод 5 привычек на страницу

    def get_queryset(self):
        """
        Вывод публичных привычек
        """
        queryset = Habit.objects.filter(sign_of_publicity=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    контроллер вывода одной привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    контроллер изменения привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    контроллер удаления     привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
