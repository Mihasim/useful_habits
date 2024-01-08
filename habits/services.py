import requests
from django.conf import settings

from config.settings import TELEGRAM_BOT_API_KEY
from habits.models import Habit
from users.models import User


def check_chat_id():
    """
    Получаение id чата
    """
    url_get_updates = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/getUpdates"
    response = requests.get(url_get_updates)
    if response.status_code == 200:
        for users in response.json()["result"]:
            user_chat_id = users["message"]["from"]["id"]
            telegram_id = '@'+users["message"]["from"]["username"]
            user = User.objects.get(telegram_id=telegram_id)
            if user.chat_id is None:
                user.chat_id = user_chat_id
                user.save()


def send_message():
    """
    Отправка сообщений с помощью телеграмм бота
    """
    check_chat_id()
    habits = Habit.objects.all()
    for habit in habits:
        try:
            chat_id = habit.user.chat_id
            new_message = f'я буду {habit.action} в {habit.time} {habit.place}. {habit.user.chat_id}'
            url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage?chat_id={chat_id}&text={new_message}"
            print(requests.get(url).json())  # Эта строка отсылает сообщение
        except(AttributeError):
            pass
