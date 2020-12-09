# Реализовать структуру данных "Товары". Она должна представлять собой список кортежей. Каждый картеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента -- номер товара и словарь с параметрами (характеристиками
# товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все
# данные у пользователя.
# Пример готовой структуры:
# [
# (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
# (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
# (1, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ -- характеристика товара, например
# название, а значение -- список значений-характеристик, например, список названий товаров.
# Пример:
# {
# 'название': ['компьютер', ' принтер', 'сканер'],
# 'цена': [20000, 6000, 2000],
# 'количество': [5, 2, 7],
# 'ед': ['шт.']
# }

# goods = []
#
# itemNumber = 1

goods = [
    (1, {'название': 'компьютер', 'цена': 20000.0, 'количество': 5, 'ед.': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000.0, 'количество': 2, 'ед.': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000.0, 'количество': 7, 'ед.': 'шт.'})
    ]

itemNumber = 4
moreItems = ''

while moreItems == '':
    moreItems = input('Введите любой знак, чтобы перейти к аналитике,\n'
                      'или нажмите \'Enter\' для ввода ещё одной позиции: ')
    if moreItems != '':
        break
    goods.append(
        (itemNumber,
         {
             'название': input(f'Введите название позиции {itemNumber}: '),
             'цена': float(input(f'Введите цену единицы товара {itemNumber}: ')),
             'количество': int(input(f'Введите количество товара {itemNumber}: ')),
             'ед.': input(f'Введите название единицы товара {itemNumber}: ')
             }
         )
        )
    itemNumber += 1

uniqueItems = set()
uniquePrice = set()
uniqueQuantity = set()
uniqueUnitName = set()

for product in goods:
    if product[1].get('название') not in uniqueItems:
        uniqueItems.add(product[1].get('название'))

for product in goods:
    if product[1].get('цена') not in uniquePrice:
        uniquePrice.add(product[1].get('цена'))

for product in goods:
    if product[1].get('количество') not in uniqueQuantity:
        uniqueQuantity.add(product[1].get('количество'))

for product in goods:
    if product[1].get('ед.') not in uniqueUnitName:
        uniqueUnitName.add(product[1].get('ед.'))

analytics = {'название': uniqueItems,
             'цена': uniquePrice,
             'количество': uniqueQuantity,
             'ед.': uniqueUnitName}

print(analytics)