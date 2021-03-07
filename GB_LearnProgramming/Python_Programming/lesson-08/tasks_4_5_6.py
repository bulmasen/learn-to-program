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
    def __init__(self, width, height, depth, weight, brand=None):
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight
        self.brand = brand


class Printer(OfficeEquipment):
    def __init__(self, color=False, laser=False):
        self.color = color
        self.laser = laser
        super().__init__(width, height, depth, weight, brand=None)


class Scanner(OfficeEquipment):
    def __init__(self, resolution_dpi, color=False):
        self.resolution_dpi = resolution_dpi
        self.color = color
        super().__init__(width, height, depth, weight, brand=None)


class Copier(OfficeEquipment):
    def __init__(self, color=False):
        self.color = color
        super().__init__(width, height, depth, weight, brand=None)


class Warehouse:
    pass
