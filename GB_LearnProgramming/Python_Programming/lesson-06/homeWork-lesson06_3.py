# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров).

workers = [
    {'wage': 30000, 'bonus': 10000}
]


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = workers


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.wage = float(wage)
        self.bonus = float(bonus)
        self.income = wage + bonus
        super().__init__(name, surname, position, self.income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'
