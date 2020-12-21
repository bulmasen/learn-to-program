# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить
# работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def coating_weight(self, thickness, weight=2400):
        """(number[, number]) -> float
        Returns the total weight of coating needed for the road.
        You can specify the weight of a cubic meter of coating.
        """
        return self.__length * self.__width * thickness * weight / 100


example_road = Road(5000, 20)
print(f'Масса асфальта, для дороги длиной 5000м, шириной 20м и толщиной 5см: \
{example_road.coating_weight(5, 2500) / 1000:.1f}т')
