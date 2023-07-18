from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from FinalProject.destinations.models import DreamDestination

UserModel = get_user_model()


class DreamDestinationsViewTests(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(username='test_user', password='test_password')

    def test_dream_destinations_view_working(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('dream destinations', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/dream-destinations.html')

    # Integration test:
    def test_dream_destinations_with_no_destinations_expect_empty_dream_destinations(self):
        # Arrange:
        self.client.login(username='test_user', password='test_password')

        # Act:
        response = self.client.get(reverse('dream destinations', kwargs={'pk': 1}))

        # Assert:
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/dream-destinations.html')
        self.assertEqual(0, response.context['dream_destinations'].count())

    # Integration test:
    def test_dream_destinations_with_one_destination(self):
        self.client.login(username='test_user', password='test_password')
        VALID_DATA = {
            'location': 'Maldives',
            'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
            'user': self.user
        }
        DreamDestination.objects.create(**VALID_DATA)

        response = self.client.get(reverse('dream destinations', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations/dream-destinations.html')
        self.assertEqual(1, response.context['dream_destinations'].count())

