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
    def __init__(self, speed=0, color='неизвестный', name='безымянный', is_police=False):
        self.speed = float(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)

    def go(self):
        print(f'Машина "{self.name}" поехала.')

    def stop(self):
        print(f'Машина "{self.name}" остановилась.')

    def turn(self, direction):
        print(f'Машина "{self.name}" повернула {direction}.')

    def show_speed(self):
        print(f'Скорость машины "{self.name}": {self.speed}')


class TownCar(Car):
    def __init__(self, speed=0, color='неизвестный', name='безымянный'):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость машины "{self.name}": {self.speed} (превышена на {self.speed - 60}).')
        else:
            print(f'Скорость машины "{self.name}": {self.speed}')


class SportCar(Car):
    def __init__(self, speed=0, color='неизвестный', name='безымянный'):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed=0, color='неизвестный', name='безымянный'):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость машины "{self.name}": {self.speed} (превышена на {self.speed - 40}).')
        else:
            print(f'Скорость машины "{self.name}": {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed=0, color='синий', name='полицейская'):
        super().__init__(speed, color, name, True)


example_car = Car()
sport_car = SportCar(210, 'красный', 'Порше')
town_car = TownCar(50, 'чёрный', 'лимузин')
work_car = WorkCar(55, 'белый', 'Газель')
police_car = PoliceCar(205)

sport_car.go()
town_car.turn('направо')
work_car.show_speed()
police_car.stop()
