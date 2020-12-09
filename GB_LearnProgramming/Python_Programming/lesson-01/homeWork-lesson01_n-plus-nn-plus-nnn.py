# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

digitN = str(int(input('Введите число n')))

digitN_and_NN_and_NNN = int(digitN) + int(digitN * 2) + int(digitN * 3)

print(f'n + nn + nnn = {digitN_and_NN_and_NNN}')
