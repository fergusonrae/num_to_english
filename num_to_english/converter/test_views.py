from django.test import TestCase
from django.urls import reverse
import os
print("settings module", os.environ['DJANGO_SETTINGS_MODULE'])

class MyTests(TestCase):
    def test_num_to_english_get_code(self):
        response = self.client.get(reverse('num_to_english_get'))
        assert response.status_code == 400
