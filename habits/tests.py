from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User

time = '15:27:57.784614'


class HabitsCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='где-то',
            time=time,
            action='поесть',
            sign_of_a_pleasant_habit=False,
            periodicity='daily',
            award='вкусняшка',
            time_to_complete=120,
            sign_of_publicity=False
        )

    def test_create_habit(self):
        """
        тестирование создания привычки
        :return:
        """
        data = {
            'user': 1,
            'place': 'где-то1',
            'time': time,
            'action': 'поесть1',
            'sign_of_a_pleasant_habit': False,
            'periodicity': 'daily',
            'award': 'вкусняшка',
            'time_to_complete': 120,
            'sign_of_publicity': False
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'related_habit': None,
                'user': 1,
                'place': 'где-то1',
                'time': time,
                'action': 'поесть1',
                'sign_of_a_pleasant_habit': False,
                'periodicity': 'daily',
                'award': 'вкусняшка',
                'time_to_complete': 120,
                'sign_of_publicity': False}
        )


class HabitsViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='где-то',
            time=time,
            action='поесть',
            sign_of_a_pleasant_habit=False,
            periodicity='daily',
            award='вкусняшка',
            time_to_complete=120,
            sign_of_publicity=False
        )

    def test_view_habit(self):
        """
        тестирование вывода привычек
        :return:
        """
        response = self.client.get(
            '/habit/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.habit.id, 'place': 'где-то', 'time': '15:27:57.784614', 'action': 'поесть',
                 'sign_of_a_pleasant_habit': False, 'periodicity': 'daily', 'award': 'вкусняшка',
                 'time_to_complete': 120, 'sign_of_publicity': False, 'user': self.user.id, 'related_habit': None}]}
        )


class HabitsRetrieveViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='где-то',
            time=time,
            action='поесть',
            sign_of_a_pleasant_habit=False,
            periodicity='daily',
            award='вкусняшка',
            time_to_complete=120,
            sign_of_publicity=False
        )

    def test_retrieve_view_habit(self):
        """
        тестирование вывода одной привычки
        :return:
        """
        response = self.client.get(
            f'/habit/{self.habit.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(
            response.json(),

            {'id': self.habit.id, 'place': 'где-то', 'time': '15:27:57.784614', 'action': 'поесть',
             'sign_of_a_pleasant_habit': False, 'periodicity': 'daily', 'award': 'вкусняшка',
             'time_to_complete': 120, 'sign_of_publicity': False, 'user': self.user.id, 'related_habit': None}
        )


class HabitsUpdateViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='где-то',
            time=time,
            action='поесть',
            sign_of_a_pleasant_habit=False,
            periodicity='daily',
            award='вкусняшка',
            time_to_complete=120,
            sign_of_publicity=False
        )

    def test_update_view_habit(self):
        """
        тестирование изменения привычки
        :return:
        """
        data = {
            'user': self.user.id,
            'place': 'где-то1',
            'time': time,
            'action': 'поесть1',
            'sign_of_a_pleasant_habit': False,
            'periodicity': 'daily',
            'award': 'вкусняшка',
            'time_to_complete': 120,
            'sign_of_publicity': False
        }

        response = self.client.put(
            f'/habit/update/{self.habit.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        self.assertEqual(
            response.json(),

            {'id': self.habit.id, 'place': 'где-то1', 'time': '15:27:57.784614', 'action': 'поесть1',
             'sign_of_a_pleasant_habit': False, 'periodicity': 'daily', 'award': 'вкусняшка',
             'time_to_complete': 120, 'sign_of_publicity': False, 'user': self.user.id, 'related_habit': None}
        )


class HabitsDestroyTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='где-то',
            time=time,
            action='поесть',
            sign_of_a_pleasant_habit=False,
            periodicity='daily',
            award='вкусняшка',
            time_to_complete=120,
            sign_of_publicity=False
        )

    def test_destroy_view_habit(self):
        """
        тестирование удаления привычки
        :return:
        """
        response = self.client.delete(
            f'/habit/delete/{self.habit.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Habit.objects.count(), 0
        )
