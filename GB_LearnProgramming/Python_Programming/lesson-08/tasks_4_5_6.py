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
from abc import ABC


class OfficeEquipment(ABC):
    def __init__(self, brand_model, device_characteristics, quantity=1):
        self.device = {'device_type': '',
                       'brand_model': brand_model,
                       'device_characteristics': device_characteristics}
        self.quantity = quantity

    def __str__(self):
        return f"{self.device['device_type'].capitalize()} {self.device['brand_model'][0]} {self.device['brand_model'][0]} - {self.quantity}"


class UnitOfOE(OfficeEquipment):
    pass


class Printer(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics, quantity=1):
        super().__init__(brand_model, device_characteristics, quantity)
        self.device.update({'device_type': 'printer'})


class Scanner(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics, quantity=1):
        super().__init__(brand_model, device_characteristics, quantity)
        self.device.update({'device_type': 'scanner'})


class Copier(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics, quantity=1):
        super().__init__(brand_model, device_characteristics, quantity)
        self.device.update({'device_type': 'copier'})

    def __str__(self):
        super().__str__()


class AllInOne(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics, quantity=1):
        super().__init__(brand_model, device_characteristics, quantity)
        self.device.update({'device_type': 'All-in-one'})

    def __str__(self):
        super().__str__()


class Warehouse:
    def __init__(self):
        self.goods = []

    def add_goods(self, item):
        if Warehouse.index_of_item_in_list(self.goods, item) is None:
            self.goods.append(item)
        else:
            self.goods[Warehouse.index_of_item_in_list(self.goods, item)][1] += item[1]

    def __iadd__(self, item):
        if isinstance(item, OfficeEquipment):
            self.add_goods(item)
        return self

    def __str__(self):
        if self.goods:
            string = ''
            for i in self.goods:
                string += f'\n\t{i}'
            return string
        else:
            return 'This warehouse is empty.'

    @staticmethod
    def index_of_item_in_list(list_of_goods, item):
        """(list_of_goods, any) -> number
        Returns index of first encountered item in list_of_goods
        >>> Warehouse.index_of_item_in_list([5, 4, 3, 4, 5], 4)
        1
        """
        counter = 0
        for i in list_of_goods:
            if i != item:
                counter += 1
            else:
                return counter
        return None

    def transfer(self, item, quantity, from_warehouse):
        pass


main_warehouse = Warehouse()
spare_warehouse = Warehouse()

aio1 = AllInOne(['Canon', 'MP-495 Series'], {'device_color': 'Black', 'print_technology': 'jet', 'color': True})
cop1 = Copier(['Canon', 'imageRUNNER 2206'], {'device_color': 'White', 'color':False}, 2)
main_warehouse += aio1
main_warehouse += cop1
print(f'Основной склад:\n'
      f'\t{main_warehouse}'
      f'Дополнительный склад:\n'
      f'\t{spare_warehouse}')
spare_warehouse.transfer(aio1, 1, main_warehouse)
print(f'После пересылки на основном складе хранится:\n'
      f'{main_warehouse}\n'
      f'На дополнительном:\n'
      f'{spare_warehouse}')
