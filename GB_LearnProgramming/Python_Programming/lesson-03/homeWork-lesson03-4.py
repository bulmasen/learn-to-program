# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
# более сложная реализация без оператора **, предусматривающая использование цикла.

def exp(x, y):
    """(number, int) -> float

    Returns the result of raising of number 'x' to the power of 'y'.
    >>> exp(2, -2)
    0.25
    >>> exp(2, 2)
    4
    """
    if y == 0:
        return 1
    if y > 0:
        for n in range(y-1):
            x *= x
        return x
    y = (-y)
    for n in range(y-1):
        x *= x
    return 1 / x


try:
    base = input('Введите основание: ')
    power = int(input('Введите степень: '))
    print(f'Результат: {exp(float(base), power)}')
except (TypeError, ValueError):
    print('Ошибочный аргумент.')
