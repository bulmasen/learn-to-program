"""
    4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
    уникальные для каждого типа оргтехники.
    5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
    в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
    других данных, можно использовать любую подходящую структуру, например словарь.
    6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
    для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
    на уроках по ООП.
"""


class OfficeEquipment:
    def __init__(self, width, height, depth, weight, brand, model, device_color, color=True):
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight
        self.brand = brand
        self.model = model
        self.device_color = device_color
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, width, height, depth, weight, brand, model, device_color, print_technology, color=True):
        self.print_technology = print_technology
        super().__init__(width, height, depth, weight, brand, model, device_color, color)


class Scanner(OfficeEquipment):
    def __init__(self, width, height, depth, weight, brand, model, device_color, resolution_dpi, color=True):
        self.resolution_dpi = resolution_dpi
        super().__init__(width, height, depth, weight, brand, model, device_color, color)

    def __str__(self):
        if not self.color:
            color = 'чёрно-белый'
        else:
            color = 'цветной'
        return f'{self.device_color.capitalize()} сканер "{self.brand}" {self.model} ({color})\n' \
               f'\t{self.width}мм/{self.height}мм/{self.depth}мм весом {self.weight}г, разрешение: ' \
               f'{self.resolution_dpi} dpi\n '


class Copier(OfficeEquipment):
    def __init__(self, width, height, depth, weight, brand, model, device_color, color=True):
        super().__init__(width, height, depth, weight, brand, model, device_color, color)

    def __str__(self):
        if not self.color:
            color = 'чёрно-белый'
        else:
            color = 'цветной'
        return f'{self.device_color.capitalize()} копир "{self.brand}" {self.model} ({color})\n' \
               f'\t{self.width}мм/{self.height}мм/{self.depth}мм весом {self.weight}г\n'


class AllInOne(OfficeEquipment):
    def __init__(self, width, height, depth, weight, brand, model, device_color, print_technology, color=True):
        self.print_technology = print_technology
        self.color = color
        super().__init__(width, height, depth, weight, brand, model, device_color, color)

    def __str__(self):
        if not self.color:
            color = 'чёрно-белый'
        else:
            color = 'цветной'
        return f'{self.device_color.capitalize()} All-in-one "{self.brand}" {self.model} ({color})\n' \
               f'\t{self.width}мм/{self.height}мм/{self.depth}мм весом {self.weight}г\n'


class Warehouse:
    def __init__(self):
        self.goods = []

    def add_goods(self, item):
        self.goods.append(item)

    def sub_goods(self, item):
        self.goods.pop(item)

    def __iadd__(self, something):
        if isinstance(something, OfficeEquipment):
            self.goods.append(something)
        return self

    def __str__(self):
        if self.goods:
            string = 'На складе хранится:\n'
            for i in self.goods:
                string += f'\n\t{i}'
            return string
        else:
            return 'Склад пуст.'


main_warehouse = Warehouse()
spare_warehouse = Warehouse()

aio1 = AllInOne(300, 100, 250, 2500, 'Canon', 'MP-495 Series', 'Black', 'Jet', True)
cop1 = Copier(622, 589, 502, 28700, 'Canon', 'imageRUNNER 2206', 'White', False)
main_warehouse += aio1
main_warehouse += cop1
print(f'Основной склад:\n'
      f'\t{main_warehouse}')
print(f'Дополнительный склад:\n'
      f'\t{spare_warehouse}')
