# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._Worker__income.get('wage') + self._Worker__income.get('bonus')


worker1 = Worker('Ихтиандр', 'Распутин', 'менеджер', 100000)
position1 = Position('Гргорый', 'Степанов', 'Парфюмер', 130000, 28000)
print(position1.get_full_name())
print(f'Общий доход: {position1.get_total_income():.2f}')
