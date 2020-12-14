# This Python file uses the following encoding: utf-8
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def calc_wage(hours, rate, bonus=0):
    """ (number, number[, number]) -> number

    Returns the calculation of the employee's pay.

    >>> calc_wage(60,1000,2000)
    62000.0
    >>> calc_wage(5.5,750,500)
    4625.0
    """
    try:
        return float(hours) * float(rate) + float(bonus)
    except ValueError:
        print('Ошибка в исходных данных.')
        return None


if len(argv) > 4:
    print('Слишком много параметров.')
elif len(argv) < 3:
    print('Не введены необходимые параметры')
elif len(argv) == 3:
    scr, a, b = argv
    print(f'Гонорар: {calc_wage(a, b):.2f}')
else:
    scr, a, b, c = argv
    print(f'Гонорар: {calc_wage(a, b, c):.2f}')
