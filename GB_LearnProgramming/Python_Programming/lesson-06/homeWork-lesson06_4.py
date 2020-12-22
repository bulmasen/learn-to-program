# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
# 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.

class Car:
    horse_power = 735.49875 / 16  # В предметной области разбираюсь слабо, так что забрал формулы

    def __init__(self, engine_power, mass, is_police=False, color='неизвестного цвета', name='безымянный'):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.engine_power = engine_power
        self.mass = mass

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {self.direction}')


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


example_car = Car('синий', 'лимузин')
print(example_car)
