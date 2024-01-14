from typing import Union

# Define lists for units, tens, and teens
UNITS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def convert_number_to_english(number: Union[int, float]) -> str:
    """Converts a number to its lowercase English representation."""
    if 'e' in str(number):
        raise ValueError("Input number has too many decimal places.")

    # Special case for zero
    if number == 0:
        return "zero"

    # Special case for negative numbers
    if number < 0:
        return "negative " + convert_number_to_english(abs(number))

    # Split the number into integer and decimal parts
    integer_part = int(number)
    if '.' in str(number):
        decimal_part = str(number).split('.')[1]
    else:
        decimal_part = None
    print(number, integer_part, decimal_part)

    # Convert the integer_part to English
    result = []
    billion = integer_part // 1000000000
    million = (integer_part % 1000000000) // 1000000
    thousand = (integer_part % 1000000) // 1000
    remainder = integer_part % 1000

    if billion > 0:
        result.append(convert_less_than_thousand(billion))
        result.append("billion")
    if million > 0:
        result.append(convert_less_than_thousand(million))
        result.append("million")
    if thousand > 0:
        result.append(convert_less_than_thousand(thousand))
        result.append("thousand")
    if remainder > 0:
        result.append(convert_less_than_thousand(remainder))

    # Convert the decimal_part to English
    if decimal_part and (int(decimal_part) > 0):
        result = result if result else ["zero"]
        result.append("point")
        result.append(convert_decimal_places(decimal_part))

    return " ".join(result)


def convert_less_than_thousand(num: int) -> str:
    if num == 0:
        return ""
    if num < 10:
        return UNITS[num]
    if num < 20:
        return TEENS[num - 10]
    if num < 100:
        return TENS[num // 10] + " " + convert_less_than_thousand(num % 10)
    return UNITS[num // 100] + " hundred " + convert_less_than_thousand(num % 100)


def convert_decimal_places(decimal_nums: str):
    # Does not follow the same logic as numbers before a decimal point
    # Instead, each digit is converted individually
    result = ""
    print(decimal_nums)
    for idx, digit in enumerate(decimal_nums):
        if digit == '0':
            if int(decimal_nums[idx:]) == 0:
                break
            result += "zero "
        else:
            result += UNITS[int(digit)] + " "
    return result.strip()
