# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

translation = {'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'
               }

with open('translated.txt', 'w') as translated:
    with open('eng_strings.txt', 'r') as source:
        for source_line in source:
            translated_line = []
            for string in source_line.split():
                if string.lower() not in translation.keys():
                    translated_line.append(f'{string} ')
                else:
                    translated_line.append(f'{translation.get(string.lower())} ')
            translated.write(''.join(translated_line).capitalize().rstrip() + '\n')
