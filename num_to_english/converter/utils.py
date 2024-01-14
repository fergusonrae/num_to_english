from typing import Union

# Define lists for units, tens, and teens
UNITS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def convert_number_to_english(number: Union[int, float]) -> str:
    """Converts a number to its lowercase English representation."""

    # Special case for zero
    if number == 0:
        return "zero"

    # Function to convert a number less than 1000 to English
    def convert_less_than_thousand(num):
        if num == 0:
            return ""
        elif num < 10:
            return UNITS[num]
        elif num < 20:
            return TEENS[num - 10]
        elif num < 100:
            return TENS[num // 10] + " " + convert_less_than_thousand(num % 10)
        else:
            return UNITS[num // 100] + " hundred " + convert_less_than_thousand(num % 100)

    # Convert the number to English
    result = ""
    billion = number // 1000000000
    million = (number % 1000000000) // 1000000
    thousand = (number % 1000000) // 1000
    remainder = number % 1000

    if billion > 0:
        result += convert_less_than_thousand(billion) + " billion "
    if million > 0:
        result += convert_less_than_thousand(million) + " million "
    if thousand > 0:
        result += convert_less_than_thousand(thousand) + " thousand "
    if remainder > 0:
        result += convert_less_than_thousand(remainder)

    return result.strip()
