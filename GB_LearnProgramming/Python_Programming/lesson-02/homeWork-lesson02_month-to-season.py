# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict .

monthAsked = str.lower(input('Введите название месяца: '))

# Вариант со списком:

monthFound = False
year = [
    ['зимний', 'декабрь', 'январь', 'февраль'],
    ['весенний', 'март', 'апрель', 'май'],
    ['летний', 'июнь', 'июль', 'август'],
    ['осенний', 'сентябрь', 'октябрь', 'ноябрь']
]

for season in year:
    for month in season[1:4]:
        if monthAsked == month:
            monthFound = True
            break
    if monthFound:  # чтобы дальше не крутился цикл
        break
if not monthFound:
    print(f'Не знаю такого месяца -- {monthAsked}.')
else:
    print(f'{str.capitalize(month)} -- {season[0]} месяц.')

# Вариант со словарём:
# Я не понял, можно ли использовать вложенный tuple, с ним просто всё гораздо короче получается в таких случаях IMO.
# Вариант в списке так же мог сократить с tuple.

monthFound = False
seasonsDict = {
    ('декабрь', 'январь', 'февраль'): 'зимний',
    ('март', 'апрель', 'май'): 'весенний',
    ('июнь', 'июль', 'август'): 'летний',
    ('сентябрь', 'октябрь', 'ноябрь'): 'осенний'
}

for season in seasonsDict:
    if monthAsked in season:
        print(f'{str.capitalize(monthAsked)} -- {seasonsDict.get(season)} месяц.')
        monthFound = True
        break
if not monthFound:
    print(f'Не знаю такого месяца -- {monthAsked}.')
