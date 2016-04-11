def convert_to_celsius(fahrenheit):
    """(number) -> int

    Return the rounded to integer number of Celsius degrees equivalent to fahrenheit degrees.
    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    """

    return round((fahrenheit - 32) * 5 / 9)
