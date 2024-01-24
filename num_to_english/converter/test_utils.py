from django.test import TestCase
from parameterized import parameterized
import pytest
from .utils import convert_number_to_english

class TestUtils(TestCase):
    @parameterized.expand([
        (1, "one"),
        (12345678, "twelve million three hundred forty five thousand six hundred seventy eight"),
        (0.91233, "zero point nine one two three three"),
        (0.00000000, "zero"),
        (-1.01, "negative one point zero one"),
        (2e3, "two thousand"),
        (90.08, "ninety point zero eight"), # Make sure spacing is correct
    ])
    def test_convert_number_to_english(self, input, expected):
        assert convert_number_to_english(input) == expected

    @parameterized.expand([
        (1e-9, ValueError),
        (0.00000001, ValueError),
        (20e30, ValueError),
    ])
    def test_convert_number_to_english_raises_error(self, input, expected_exception):
        with pytest.raises(expected_exception):
            convert_number_to_english(input)
