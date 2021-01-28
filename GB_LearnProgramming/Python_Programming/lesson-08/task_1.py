"""
        1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
        строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
        декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
        типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
        месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
        реальных данных.
"""


class Date:
    def __init__(self, str_input):
        self.str_input = str_input
        try:
            self.date = Date.date_format(str_input)
            if Date.is_valid_date(self.date):
                self.day = self.date[0]
                self.month = self.date[1]
                self.year = self.date[2]
        except ValueError:
            self.date = None

    @classmethod
    def date_format(cls, date_str):
        date_formatted = []
        string_splitted = date_str.split('-')
        for i in string_splitted:
            date_formatted.append(int(i))
        if Date.is_valid_date(date_formatted):
            return date_formatted
        else:
            return None

    @staticmethod
    def is_valid_date(date):
        days_in_month = {
            1: 31,
            2: 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        """(any) -> Boolean
        Returns True if the input data matches the format [valid date, valid month, valid year].
        Leap years are not counted, February 29 is always valid.
        
        Prerequisite: year in the range 1920-2021

        >>> is_valid_date([ds,ds,da])
        False
        >>> is_valid_date([02.12.2008])
        True
        >>> is_valid_date([03.17.-3000])
        False
        """
        if not date:
            return False
        if len(date) == 3 and \
                1 <= date[0] <= days_in_month[date[1]] and \
                date[2] in range(1920, 2021):
            return True
        else:
            return False

    def __str__(self):
        if Date.is_valid_date(self.date):
            return f'{self.day:02}-{self.month:02}-{self.year:04}'
        else:
            return f'{self.str_input} is not valid formatted date.'


input1 = '20-02-1980'
input2 = 'ds-sas-sa'
input3 = '35-02-11'
date1 = Date(input1)
date2 = Date(input2)
date3 = Date(input3)
print(f'{input1} => {date1}\n'
      f'{input2} => {date2}\n'
      f'{input3} => {date3}')
