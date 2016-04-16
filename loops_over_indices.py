def shift_left(l):
    """ (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    """

    first_item = l[0]

    for i in range(1, len(l)):
        l[i - 1] = l[i]

    l[-1] = first_item


def count_adjacent_repeats(s):
    """ (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    """

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats += 1

    return repeats
