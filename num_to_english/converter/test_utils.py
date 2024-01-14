import pytest
from .utils import convert_number_to_english


@pytest.mark.parametrize("input,expected", [
    (1, "one"),
    (12345678, "twelve million three hundred forty five thousand six hundred seventy eight"),
    (0.91233, "zero point nine one two three three"),
    (0.00000000, "zero"),
    (-1.01, "negative one point zero one"),
])
def test_convert_number_to_english(input, expected):
    assert convert_number_to_english(input) == expected


@pytest.mark.parametrize("input, expected_exception", [
    (1e-9, ValueError),
    (0.00000001, ValueError),
])
def test_convert_number_to_english_raises_error(input, expected_exception):
    with pytest.raises(expected_exception):
        convert_number_to_english(input)
