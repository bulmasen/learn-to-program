# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

varA = 1
varB = 'B'
print(f'Первая сохранённая переменная: {varA}\nВторая сохранённая переменная: {varB}\n')

varIntegerNumber = int(input('Введите целое число: '))
varString = str(input('Введите строку: '))
varFloatingNumber = float(input('Введите десятичную дробь: '))

print(f'Первая переменная: {varIntegerNumber} - {type(varIntegerNumber)}')
print(f'Вторая переменная: {varString} - {type(varString)}')
print(f'Третья переменная: {varFloatingNumber} - {type(varFloatingNumber)}')
