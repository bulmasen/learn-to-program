# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

from random import randint, random
from functools import reduce
from os.path import abspath

s1 = 'proc_file.txt'

with open(s1, 'w') as proc_file:
    for i in range(randint(10, 40)):
        for i2 in range(randint(10, 15)):
            proc_file.write(f'{round(random() * 10, 2)} ')
        proc_file.seek(proc_file.tell() - 1)
        proc_file.write('\n')

with open(s1, 'r') as proc_file:
    result = 0
    for line in proc_file:
        nums_in_line = line.split()
        result += reduce(lambda a, b: a + b, [float(el) for el in nums_in_line])

print(f'Сумма цифр в файле\n{abspath(s1)}\nравна {round(result, 2)}')
