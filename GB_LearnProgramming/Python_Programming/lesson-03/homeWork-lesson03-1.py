# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(number, divisor):
    """ (number, number) -> float

    Simple division.

    Pre-condition: divisor != 0

    >>> division(4, 2)
    2.0
    >>> division(9, 0)
    Ошибка деления на ноль.
    >>> division(True, '')
    Ошибка формата аргумента.
    """
    try:
        result = number / divisor
    except ZeroDivisionError:
        print('Ошибка деления на ноль.')
        return None
    except TypeError:
        print('Ошибка формата аргумента.')
        return None
    return result
