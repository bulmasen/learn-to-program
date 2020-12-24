from random import randint
from abc import ABC, abstractmethod


# abc - abstract Base Class


class Send(ABC):

    @abstractmethod
    def postcode(self):
        pass


class Stiffness(ABC):

    @abstractmethod
    def corner(self):
        pass


class Box(Send):

    def __init__(self):
        self.__postcode = '$' + str(randint(100000, 999999))

    @property
    def postcode(self):
        return self.__postcode

    def __str__(self):
        return f'Postcode: {self.__postcode}'
