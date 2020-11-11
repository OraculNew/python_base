"""
PEP-8
"""
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @class method, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца 
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
# Код программы


class Date:

    @classmethod
    def read_date(cls, str_date):
        return [int(itm) for itm in str_date.split("-")]

    @staticmethod
    def validate(str_date):
        list_date = Date.read_date(str_date)
        day, month, year = list_date[0], list_date[1], list_date[2]
        _days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        _is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        if month == 2 and _is_leap:
            days = 29
        else:
            days = _days_in_month[month]

        return 1 <= day <= days and 1 <= month <= 12 and 1 <= year <= 9999


str_d = "29-02-2020"
list_d = Date.read_date(str_d)
print(f"{list_d[0]}-{list_d[1]}-{list_d[2]}")
print(Date.validate(str_d))

str_d = "29-2-2021"
list_d = Date.read_date(str_d)
print(f"{list_d[0]}-{list_d[1]}-{list_d[2]}")
print(Date.validate(str_d))
