from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_message, check_chat_id


@shared_task
def check_date():
    habits = Habit.objects.all()
    for habit in habits:
        if habit.periodicity == 'daily' and datetime.now().weekday() == 1:
            send_message()

            if (habit.periodicity == 'every_two_days' and datetime.now().weekday() == 0
                    or datetime.now().weekday() == 2 or datetime.now().weekday() == 4):
                send_message()

            if (habit.periodicity == 'every_three_days' and datetime.now().weekday() == 0
                    or datetime.now().weekday() == 3 or datetime.now().weekday() == 5):
                send_message()

            if (habit.periodicity == 'every_four_days' and datetime.now().weekday() == 0
                    or datetime.now().weekday() == 3):
                send_message()

            if (habit.periodicity == 'every_five_days' and datetime.now().weekday() == 0
                    or datetime.now().weekday() == 4):
                send_message()

            if (habit.periodicity == 'every_six_days' and datetime.now().weekday() == 0
                    or datetime.now().weekday() == 5):
                send_message()

            if habit.periodicity == 'once_a_week' and datetime.now().weekday() == 1:
                send_message()


@shared_task
def test():
    check_chat_id()
    send_message()
