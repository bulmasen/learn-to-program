"""
Реализовать программу работы с органическими клетками. Необходимо создать
класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки
определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр
класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки
по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество
ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда
метод make_order() вернет строку: *****\n*****\n*****.

Подсказка: подробный список операторов для перегрузки доступен по ссылке
https://pythonworld.ru/osnovy/peregruzka-operatorov.html
"""


class Entity:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        if isinstance(other, Entity):
            return self.cells + other.cells
        else:
            return self

    def __sub__(self, other):
        if isinstance(other, Entity):
            if self.cells < other.cells:
                return None
            else:
                return self.cells - other.cells
        else:
            return self

    def __mul__(self, other):
        if isinstance(other, Entity):
            return self.cells * other.cells
        else:
            return self

    def __truediv__(self, other):
        if isinstance(other, Entity) and other.cells > 0:
            if self.cells // other.cells == 0:
                return None
            else:
                return self.cells // other.cells
        else:
            return self

    def __str__(self):
        if self.cells:
            return f'{self.cells} cells'
        else:
            return 'The entity has vanished'

    def make_order(self, columns):
        rows = self.cells // columns
        tail = int(self.cells % columns)
        return ('*' * columns + '\n') * rows + '*' * tail


# e1 = Entity('Задайте количество ячеек в первой клетке:')
# e2 = Entity('Задайте количество ячеек в второй клетке:')
e1 = Entity(27)
e2 = Entity(38)
e3_sum = Entity(e1 + e2)
e4_sub = Entity(e1 - e2)
e5_div = Entity(e1 / e2)
e6_mul = Entity(e1 * e2)
print(f'первый по 5:\n{e1.make_order(5)}\n'
      f'второй по 6:\n{e2.make_order(6)}\n'
      f'Addition: {e3_sum},\n'
      f'Subtraction: {e4_sub},\n'
      f'Division: {e5_div},\n'
      f'Multiplication: {e6_mul}\n')
