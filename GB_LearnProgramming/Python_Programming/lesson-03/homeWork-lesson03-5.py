# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def add_numbers(numbers):
    """ (tuple of num) -> float

    Returns the sum of numbers.

    >>> add_numbers([33, 55.5, -1])
    87.5
    """
    total = 0
    for item in numbers:
        try:
            total += float(item)
        except (ValueError, SyntaxError):
            print('Ошибочный аргумент, добавление не произведено.')
            return 0
    return total


grandTotal = 0
endString = False

request = input('Для добавления введите разделённые пробелом цифры и \'q\' для завершения расчёта:\n').split()

while True:
    if 'q' in request:
        for index in range(len(request)):
            if request[index] == 'q':
                del request[index:]
                endString = True
                break
    if not request:
        break
    try:
        grandTotal += add_numbers(tuple(request))
    except SyntaxError:
        print('Ошибка ввода, добавление не произведено.')
        continue
    print(f'Сумма чисел = {grandTotal}')
    if endString:
        break
    request = input().split()
