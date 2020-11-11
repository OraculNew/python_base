"""
PEP-8
"""
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""
# Код программы


class MyZeroDivisionError(ArithmeticError):
    pass


def my_div(a: float, b: float):
    try:
        try:
            return a/b
        except ZeroDivisionError:
            raise MyZeroDivisionError()
    except MyZeroDivisionError:
        # print("Second argument to a division or modulo operation was zero.")
        return float("inf")


print(my_div(float(input("Введите числитель\n>>>")), float(input("Введите знаменатель\n>>>"))))
