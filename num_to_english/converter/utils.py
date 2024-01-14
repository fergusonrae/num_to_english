import logging
from typing import Union

logger = logging.getLogger(__name__)

# Define lists for units, tens, and teens
UNITS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def convert_number_to_english(number: Union[int, float]) -> str:
    """Converts a number to its lowercase English representation."""

    # special cases
    if 'e' in str(number):
        logger.info(f"Number {number} is too large or has too many decimal places.")
        raise ValueError("Input number is too large or has too many decimal places.")
    if number == 0:
        return "zero"
    if number < 0:
        return f"negative {convert_number_to_english(abs(number))}"

    # Split the number into integer and decimal parts
    # Use string for decimal part to avoid floating point errors
    integer_part = int(number)
    decimal_part = str(number).split('.')[1] if len(str(number).split('.')) > 1 else None

    # Convert the integer_part to English
    result = convert_integer_to_english(integer_part)

    # Convert the decimal_part to English
    if decimal_part:
        result = result if result else ["zero"]
        decimals_as_str = convert_decimal_places(decimal_part)
        if decimals_as_str:
            result.append("point")
            result.extend(decimals_as_str)

    return " ".join(result)


def convert_integer_to_english(integer_part: int) -> str:
    result = []
    billion = integer_part // 1000000000
    million = (integer_part % 1000000000) // 1000000
    thousand = (integer_part % 1000000) // 1000
    remainder = integer_part % 1000

    if billion > 0:
        result.extend(convert_less_than_thousand(billion))
        result.append("billion")
    if million > 0:
        result.extend(convert_less_than_thousand(million))
        result.append("million")
    if thousand > 0:
        result.extend(convert_less_than_thousand(thousand))
        result.append("thousand")
    if remainder > 0:
        result.extend(convert_less_than_thousand(remainder))
    return result

def convert_less_than_thousand(num: int) -> list:
    if num == 0:
        return []
    if num < 10:
        return [UNITS[num]]
    if num < 20:
        return [TEENS[num - 10]]
    if num < 100:
        return [TENS[num // 10]] + convert_less_than_thousand(num % 10)
    return [UNITS[num // 100], "hundred"] + convert_less_than_thousand(num % 100)


def convert_decimal_places(decimal_nums: str) -> list:
    # Does not follow the same logic as numbers before a decimal point
    # Instead, each digit is converted individually
    result = []
    for digit in decimal_nums.rstrip('0'):
        if digit == '0':
            result.append("zero")
        else:
            result.append(UNITS[int(digit)])
    return result
