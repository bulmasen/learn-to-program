def special_list_handler(numbers_list):
    """ (list of numbers) -> list of numbers

    Returns a list of elements in the source list with values greater than the
    previous element in the source list.

    >>> special_list_handler([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
    [12, 44, 4, 10, 78, 123]
    """
    return [numbers_list[index] for index in range(1, len(numbers_list))\
            if numbers_list[index] > numbers_list[index-1]]
