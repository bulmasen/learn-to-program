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
        except ValueError:
            self.date = None
        if Date.is_valid_date(self.date):
            self.day = self.date[0]
            self.month = self.date[1]
            self.year = self.date[2]

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
        """(list) -> Boolean
        Returns True if the input data matches the format [valid day, valid month, valid year].
        
        Prerequisite: year in the range 1920-2021. Leap years are not counted, February 29 is always valid.

        >>> print(Date.is_valid_date([2, 12, 2008]))
        True
        >>> print(Date.is_valid_date([3, 17, -3000]))
        False
        """
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
        if not date:
            return False
        try:
            if len(date) == 3 and \
                1 <= date[0] <= days_in_month[date[1]] and \
                    date[2] in range(1920, 2021):
                return True
            else:
                return False
        except KeyError:
            return False

    def __str__(self):
        if Date.is_valid_date(self.date):
            month_names = {1: 'января',
                           2: 'февраля',
                           3: 'марта',
                           4: 'апреля',
                           5: 'мая',
                           6: 'июня',
                           7: 'июля',
                           8: 'августа',
                           9: 'сентября',
                           10: 'октября',
                           11: 'ноября',
                           12: 'декабря'}
            return f'{self.day:02} {month_names[self.month]} {self.year:04}г.'
        else:
            return f'{self.str_input} is not valid formatted date.'


date1 = Date('20-02-1980')
date2 = Date('ds-sas-sa')
date3 = Date('35-02-11')
print(f'\'{date1.str_input}\' => {date1}\n'
      f'\'{date2.str_input}\' => {date2}\n'
      f'\'{date3.str_input}\' => {date3}')
