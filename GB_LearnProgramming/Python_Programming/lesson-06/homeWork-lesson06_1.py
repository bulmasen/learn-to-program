# Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
# метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго
# (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение
# между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
# описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self, red_light=7, yellow_light=2, green_light=5):
        self.light_time = {
            'red': red_light,
            'yellow': yellow_light,
            'green': green_light
        }

    def running(self):
        for i in cycle(['red', 'yellow', 'green', 'yellow']):
            print(i)
            sleep(self.light_time.get(i))


traffic_light = TrafficLight()
traffic_light.running()
