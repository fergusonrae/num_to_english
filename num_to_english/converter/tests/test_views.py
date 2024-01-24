from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

class TestViews(TestCase):
    @parameterized.expand([
        ({'number': '1'}, 200),
        ({'number': '-1'}, 200),
        ({'number': '1.09'}, 200),
        (None, 400),
        ({'number': ''}, 400),
        ({'number': str(1e20)}, 400),
    ])
    def test_num_to_english_code(self, input, status_code):
        get_response = self.client.get(reverse('num_to_english'), data=input)
        post_response = self.client.post(reverse('num_to_english'), data=input)
        assert get_response.status_code == status_code
        assert post_response.status_code == status_code
