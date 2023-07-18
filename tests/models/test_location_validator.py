from django.contrib.auth import get_user_model
from django.test import TestCase  # django.test contains the unittest
from django.core.exceptions import ValidationError
from FinalProject.destinations.models import DreamDestination

UserModel = get_user_model()


class LocationTests(TestCase):
    VALID_DATA = {
        'location': 'Maldives',
        'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
    }

    LONG_LOCATION_DATA = {
        'location': 31 * "A",
        'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
    }

    SHORT_LOCATION_DATA = {
        'location': "A",
        'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
    }

    NONE_LOCATION_DATA = {
        'location': None,
        'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
    }

    WITH_DIGIT_LOCATION_DATA = {
        'location': "Dubai5",
        'place_photo': 'https://d2bgjx2gb489de.cloudfront.net/gbb-blogs/wp-content/uploads/2019/10/14185703/Ensemble-of-three-Socialist-Classicism-edifices-in-Sofia.jpg',
    }

    def setUp(self):
        self.user = UserModel.objects.create(username='test_user')
        super().setUp()

    def test_valid_location_expect_to_be_created(self):
        dream_destination = DreamDestination(**self.VALID_DATA, user=self.user)
        dream_destination.save()

        self.assertIsNotNone(dream_destination.pk)

    def test_location_has_exceeding_length(self):
        with self.assertRaises(ValidationError):
            dream_destination = DreamDestination(**self.LONG_LOCATION_DATA, user=self.user)
            dream_destination.full_clean()

    def test_location_has_less_than_2_syms_expect_raise(self):
        with self.assertRaises(ValidationError):
            dream_destination = DreamDestination(**self.SHORT_LOCATION_DATA, user=self.user)
            dream_destination.full_clean()

    def test_location_is_none_expect_to_raise(self):
        with self.assertRaises(ValidationError):
            dream_destination = DreamDestination(**self.NONE_LOCATION_DATA, user=self.user)
            dream_destination.full_clean()

    def test_location_consists_not_only_letters_to_raise(self):
        with self.assertRaises(ValidationError):
            dream_destination = DreamDestination(**self.WITH_DIGIT_LOCATION_DATA, user=self.user)
            dream_destination.full_clean()
