# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count


def fact(number):
    """(int) -> generator
    Returns a sequential factorial generator.
    >>> for el in fact(4):
    ...     print(el)
    1
    2
    6
    24
    """
    f = 1
    for m in count(1):
        f = f * m
        yield f
        if m == int(number):
            break


n = input('Введите число для расчёта факториала: ')
try:
    for element in fact(n):
        print(element)
except ValueError:
    print('Ошибка входных данных')
