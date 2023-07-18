from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError

from FinalProject.destinations.models import DreamDestination

UserModel = get_user_model()


class AddDreamDestinationsViewTests(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='test_user', password='test_password')

    def test_create_destination_when_valid_expect_success(self):
        # Arrange:
        self.client.login(username='test_user', password='test_password')
        VALID_DATA = {
            'location': 'Maldives',
            'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
            'user': self.user
        }

        # Act:
        response = self.client.post(reverse('add destination'), data=VALID_DATA)

        # Assert:
        dream_destination = DreamDestination.objects.get()
        self.assertIsNotNone(dream_destination)
        self.assertEqual(302, response.status_code)

    # def test_create_destination_when_not_valid_expect_error(self):

