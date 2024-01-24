from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_num_to_english_get_code(self):
        response = self.client.get(reverse('num_to_english_get'))
        assert response.status_code == 400
