from django.urls import path

from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

router = DefaultRouter()

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('public_habit/', PublicHabitListAPIView.as_view(), name='public_habit_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),

]
