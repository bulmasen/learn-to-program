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


class NotEnoughError(Exception):
    pass


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
        if item.is_valid_formatted and Warehouse.ext_index(self.goods, item) is None:
            self.goods.append([item, quantity])
        else:
            self.goods[Warehouse.ext_index(self.goods, item)][1] += int(quantity)

    def remove_goods(self, index, quantity=1):
        if self.goods[index][1] == int(quantity):
            self.goods.remove([index])
        elif self.goods[index][1] > int(quantity):
            self.goods[index][1] -= int(quantity)
        else:
            raise NotEnoughError

    def transfer(self, to_warehouse, item, quantity=1):
        try:
            out_item_index = Warehouse.ext_index(self.goods, item)
            self.remove_goods(out_item_index, int(quantity))
            to_warehouse.add_goods(item, int(quantity))
        except NotEnoughError:
            print(f'Недостаточно {item} на складе.')

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
    def ext_index(list_of_goods, item):
        """(list_of_lists, any) -> number
        Returns index of first encountered item in list_of_goods or None if not exist. Analog of list.index(value)
        >>> Warehouse.ext_index([[5, 3], [4, 5], [3, 1], [4, 2]], 4)
        1
        """
        counter = 0
        for i in list_of_goods:
            if i[0] != item:
                counter += 1
            else:
                return counter
        return None


########################################################################################
first_warehouse = Warehouse()
second_warehouse = Warehouse()
third_warehouse = Warehouse()

aio1 = AllInOne(['Canon', 'MP-495 Series'],
                {'device_color': 'Black',
                 'print_technology': 'jet',
                 'color': True})
cop1 = Copier(['Canon', 'imageRUNNER 2206'],
              {'device_color': 'white',
               'color': False})
prn1 = Printer(['HP', 'OfficeJet Pro 6230'],
               {'device_color': 'black',
                'print_technology': 'jet',
                'color': True})
scn1 = Scanner(['Avision', 'FB10'],
               {'device_color': 'black',
                'dpi_resolution': 600})
first_warehouse += aio1
first_warehouse += cop1
first_warehouse.add_goods(Scanner(['Avision', 'FB10'],
                                  {'device_color': 'black',
                                  'dpi_resolution': 600}))
second_warehouse.add_goods(prn1, 2)
third_warehouse += scn1
print(f'Warehouse 1:'
      f'\t{first_warehouse}'
      f'\nWarehouse 2:'
      f'\t{second_warehouse}'
      f'\nWarehouse 3:'
      f'\t{third_warehouse}')
print(f'\nTransition attempt {prn1} from 2 to 3 and\n'
      f'two of {aio1} transition from 1 to 3,\n')
second_warehouse.transfer(third_warehouse, prn1)
first_warehouse.transfer(third_warehouse, aio1, 2)
print(f'\nWarehouse 1:'
      f'\t{first_warehouse}\n'
      f'\nWarehouse 2:'
      f'\t{second_warehouse}\n'
      f'\nWarehouse 3:'
      f'\t{third_warehouse}')
