# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по
# этому предмету и их количество. Важно, чтобы для каждого предмета не
#обязательно были все типы занятий. Сформировать словарь, содержащий название
# предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                      Физика:   30(л)   —   10(лаб)
#                      Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce

subjects = {}
with open('disciplines.txt', 'r') as source_file:
    for line in source_file:
        chunks = line.split(':')
        digits = ''
        for symbol in chunks[1]:
            if symbol in '0123456789 ':
                digits += symbol
        # subjects[chunks[0]] = sum(int(el) for el in digits.split())
        subjects[chunks[0]] = sum(int(el) for el in digits.split())

print(subjects)
