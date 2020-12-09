# Для списка реализовать обмен значений соседних элементов, т.е., значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов
# необходимо использовать функцию input().

number_of_objects = int(input('Задайте размер списка: '))
mutatingList = []

for item in range(number_of_objects):
    mutatingList.append(input(f'Введите значение ячейки {item + 1} '))

for i in range(number_of_objects // 2):
    mutatingList[i * 2], mutatingList[i * 2 + 1] =\
        mutatingList[i * 2 + 1], mutatingList[i * 2]

print(mutatingList)
