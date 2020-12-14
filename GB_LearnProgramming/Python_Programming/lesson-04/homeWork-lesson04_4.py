# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы
# вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint as rnd


def clr_list_gen(old_list):
    """(list of numbers) -> list of numbers

    Returns a generator of list with repeating numbers deleted totally.

    >>> print(next(clr_list_gen([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])))
    23
    """
    return (old_list[i] for i in range(len(old_list)) if old_list.count(old_list[i]) == 1)


rand_list = [rnd(0, 20) for c in range(rnd(8, 15))]

line = 0
for el in clr_list_gen(rand_list):
    print(f'{rand_list[line]:>10} || {el}')
    line += 1
for el in range(line, len(rand_list)):
    print(f'{rand_list[line]:>10} ||')
    line += 1
