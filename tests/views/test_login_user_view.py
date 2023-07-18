from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class LoginUserViewTests(TestCase):
    def test_login_user(self):
        user_data = {
            'username': 'someone',
            'password': 'someone123456'
        }

        user = UserModel.objects.create_user(**user_data)
        self.client.login(username=user.username, password=user_data['password'])

        response = self.client.get(reverse('home page'))

        self.assertEqual(response.status_code, 200)
