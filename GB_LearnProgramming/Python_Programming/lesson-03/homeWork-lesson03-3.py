# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(a, b=0, c=0):
    """ (float, float, float) -> float

    Return sum of greater two of three numbers.
    
    >>> my_func(4, 2)
    6.0
    """
    try:
        result = float(a + b + c)
    except TypeError:
        print('Ошибка формата аргумента.')
        return None
    if a <= b & a <= c:
        return result - a
    elif b <= a & b <= c:
        return result - b
    else:
        return result - c
