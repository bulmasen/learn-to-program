# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

txt = open(r'another_file.txt', 'r')
words_counter = 0
lines_counter = 0
for line in txt:
    words_counter += len(line.split())
    lines_counter += 1
txt.close()

print(f'В файле {words_counter} слов в {lines_counter} строках.')
