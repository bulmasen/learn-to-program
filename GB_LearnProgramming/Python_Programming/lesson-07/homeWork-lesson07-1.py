"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        if type(matrix) == list:
            self.matrix = matrix
        else:
            self.matrix = []

    def sum_matrix(self, other):
        if isinstance(other, Matrix) and self.matrix and other.matrix:
            rez = []
            try:
                for i in range(len(self.matrix)):
                    rez.append([])
                    for j in range(len(self.matrix[i])):
                        rez[i].append(int(self.matrix[i][j]) + int(other.matrix[i][j]))
                return rez
            except IndexError:
                print('Ошибка несовпадения размерности матриц.')
            except ValueError:
                print('Ошибка значения в матрице.')
        else:
            return None

    def __add__(self, other):
        self.sum_matrix(other)

    def __str__(self):
        if self.matrix:
            str_out = []
            for i in self.matrix:
                str_out.append(f'|')
                for j in i:
                    str_out.append(f' {str(j):_>5}')
                str_out.append(' |\n')
            return ''.join(str_out)
        else:
            return ''


matr_1 = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
matr_2 = Matrix([[999, 888, 777],
                 [666, 555, 444],
                 [333, 222, 111]])
longer_matrix = Matrix([[1234, 2345, 3456, 4567],
                        [4567, 5678, 6789, 7890],
                        [5678, 6789, 7890, 8901]])
matrix_w_error = Matrix([[5678, 6789, 7890, 8901],
                         [4567, 5678, 6789, 7890],
                         [1234, 2345, 'sudo', 4567]])

print(f'\n_________________________________________\n'
      f'{matr_1}'
      f'\t\t+\n'
      f'{matr_2}'
      f'\t\t=')
simple_sum = Matrix(matr_1.sum_matrix(matr_2))
print(simple_sum)

print(f'\n_________________________________________\n'
      f'{longer_matrix}'
      f'\t\t+\n'
      f'{matr_2}'
      f'\t\t=')
lesser_size = Matrix(longer_matrix + matr_2)
print(lesser_size)

print(f'\n_________________________________________\n'
      f'{longer_matrix}'
      f'\t\t+\n'
      f'{matrix_w_error}'
      f'\t\t=')
data_fail = Matrix(longer_matrix + matrix_w_error)
print(data_fail)

print(f'\n_________________________________________\n'
      f'{matrix_w_error}'
      f'\t\t+\n'
      f'\t\t1\n'
      f'\t\t=')
fail2 = Matrix(matrix_w_error + {})
print(fail2)

print(f'\n_________________________________________\n'
      f'{fail2}'
      f'\t\t+\n'
      f'{matr_1}'
      f'\t\t=')
print(fail2 + matr_1)
