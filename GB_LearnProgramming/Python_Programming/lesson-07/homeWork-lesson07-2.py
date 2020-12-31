"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def fabric_expend(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_expend(self):
        return self.size / 6.5 + .5

    def __str__(self):
        return f'Пальто {self.size} размера.'


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_expend(self):
        return self.height * 2 + .3

    def __str__(self):
        return f'Костюм {self.height} роста.'


class Warehouse:
    def __init__(self):
        self.goods = []

    def add_goods(self, item):
        self.goods.append(item)

    @property
    def total_fabric(self):
        fabric = 0
        for i in self.goods:
            fabric += i.fabric_expend
        return fabric

    def __iadd__(self, something):
        if isinstance(something, Cloth):
            self.goods.append(something)
        return self

    def __str__(self):
        if self.goods:
            string = 'На складе хранится:'
            for i in self.goods:
                string += f'\n\t{i}'
            return string
        else:
            return 'Склад пуст.'


warehouse1 = Warehouse()
warehouse1.add_goods(Suit(170))
warehouse1 += Suit(175)
warehouse1 += Coat(40)
warehouse1 += Coat(42)

print(warehouse1)
print(f'Общее количества материала, затраченного на пошив хранящейся одежды: {warehouse1.total_fabric:.1f}')
