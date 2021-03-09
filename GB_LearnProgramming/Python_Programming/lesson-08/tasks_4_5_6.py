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
    def __init__(self, brand_model, device_characteristics):
        self.device = {'device_type': '',
                       'brand_model': brand_model,
                       'device_characteristics': device_characteristics}

    def __str__(self):
        return f"{self.device['device_type'].capitalize()} {self.device['brand_model'][0]} " \
               f"{self.device['brand_model'][1]}"

    @property
    def is_valid_formatted(self):
        try:
            if self.device['device_type'] and \
                    len(self.device['brand_model']) == 2 and \
                    type(self.device['device_characteristics']) == dict:
                return True
            else:
                return False
        except KeyError:
            return False


class UnitOfOE(OfficeEquipment):
    pass


class Printer(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics):
        super().__init__(brand_model, device_characteristics)
        self.device.update({'device_type': 'printer'})


class Scanner(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics):
        super().__init__(brand_model, device_characteristics)
        self.device.update({'device_type': 'scanner'})


class Copier(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics):
        super().__init__(brand_model, device_characteristics)
        self.device.update({'device_type': 'copier'})


class AllInOne(OfficeEquipment):
    def __init__(self, brand_model, device_characteristics):
        super().__init__(brand_model, device_characteristics)
        self.device.update({'device_type': 'All-in-one'})


class Warehouse:
    def __init__(self):
        self.goods = []

    def add_goods(self, item, quantity=1):
        if item.is_valid_formatted and Warehouse.index_of_item_in_list(self.goods, item) is None:
            self.goods.append([item, quantity])
        else:
            self.goods[Warehouse.index_of_item_in_list(self.goods, item)][1] += int(quantity)

    def __iadd__(self, item):
        if isinstance(item, OfficeEquipment):
            self.add_goods(item)
        return self

    def __str__(self):
        if self.goods:
            f_string = []
            for i in self.goods:
                f_string.append(f'\n\t{i[0]} - {i[1]}')
            return ''.join(f_string)
        else:
            return '\n\tThis warehouse is empty.'

    @staticmethod
    def index_of_item_in_list(list_of_goods, item):
        """(list_of_lists, any) -> number
        Returns index of first encountered item in list_of_goods or None if not exist.
        >>> Warehouse.index_of_item_in_list([[5, 3], [4, 5], [3, 1], [4, 2]], 4)
        1
        """
        counter = 0
        for i in list_of_goods:
            if i[0] != item:
                counter += 1
            else:
                return counter
        return None

    def transfer(self, item, quantity, to_warehouse):
        pass


main_warehouse = Warehouse()
spare_warehouse = Warehouse()
distant_warehouse = Warehouse()

aio1 = AllInOne(['Canon', 'MP-495 Series'],
                {'device_color': 'Black',
                 'print_technology': 'jet',
                 'color': True})
cop1 = Copier(['Canon', 'imageRUNNER 2206'],
              {'device_color': 'White',
               'color': False})
prn1 = Printer(['HP', 'OfficeJet Pro 6230'],
               {'device_color': 'Black',
                'print_technology': 'jet',
                'color': True})
main_warehouse += aio1
main_warehouse += cop1
spare_warehouse.add_goods(prn1, 2)
print(f'Warehouse 1:'
      f'\t{main_warehouse}'
      f'\nWarehouse 2:'
      f'\t{spare_warehouse}'
      f'\nWarehouse 3:'
      f'\t{distant_warehouse}')
spare_warehouse.transfer(aio1, 1, main_warehouse)
print(f'\nAfter transfer, Warehouse 1:'
      f'\t{main_warehouse}\n'
      f'\nWarehouse 2:'
      f'\t{spare_warehouse}\n'
      f'\nWarehouse 3:'
      f'\t{distant_warehouse}')
