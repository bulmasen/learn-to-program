# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если слово длинное, вводить только первые 10 букв в слове.

words = input('Введите несколько слов, разделённых пробелами:\n')

wordsList = words.split()
counter = 1

for singleWord in wordsList:
    singleWord = singleWord[:10]
    print(f'{counter}: {singleWord}')
    counter += 1