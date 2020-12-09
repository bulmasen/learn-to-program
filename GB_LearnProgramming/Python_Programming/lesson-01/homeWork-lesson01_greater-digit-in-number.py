# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while
# и арифметические операции.

number = abs(int(input('Число? ')))  # с отрицательными не работает, так что abs()

number_of_digits = 0
n = number
greater_number = 0

while n > 0:
    m = n % 10
    n = n // 10
    if m > greater_number:
        greater_number = m
    if greater_number == 9:
        break
    number_of_digits += 1

print(f'Самая большая цифра в этом числе = {greater_number}')
