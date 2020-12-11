# Реализовать функцию str_cap(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(str_cap(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию str_cap().

def str_cap(word):
    """ (string) -> string

    Return capitalized word.

    >>> str_cap('example')
    'Example'
    >>> str_cap('9')
    '9'
    >>> str_cap(True)
    Ошибочный аргумент.
    """
    try:
        return word.capitalize()
    except AttributeError:
        print('Ошибочный аргумент.')
        return None


sentence = input('Введите предложение: ')
newSentence = ''

for word in sentence.split():
    newSentence += str_cap(word) + ' '

print(newSentence.strip())
