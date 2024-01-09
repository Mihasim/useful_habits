from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_register_user(self):
        """
        тестирование регистрации
        :return:
        """
        data = {
            "email": "1234@mail.ru",
            "password": "5482",
            "password2": "5482",
            "telegram_id": "@123"
        }
        response = self.client.post(
            '/users/register/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'response': True}
        )


class UsersViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_view_user(self):
        """
        тестирование вывода пользователей
        :return:
        """
        response = self.client.get(
            '/users/user/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)


class UsersRetrieveViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.test', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_view_user(self):
        """
        тестирование вывода одного пользователя
        :return:
        """
        response = self.client.get(
            f'/users/user/{self.user.id}/',
        )
        print(self.user)
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)
