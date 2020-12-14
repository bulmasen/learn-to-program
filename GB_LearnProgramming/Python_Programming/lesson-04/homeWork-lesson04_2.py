# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from homeWork04_module import special_list_handler
from random import random, randint

print(special_list_handler([int(random() * 100) for i in range(int(random() * 20 + 5))]))
# или
print(special_list_handler([randint(0, 100) for i in range(randint(5, 20))]))
