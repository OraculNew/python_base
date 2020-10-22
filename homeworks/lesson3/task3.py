"""
PEP-8
"""
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших 
двух аргументов.
"""
# Код программы


def chek_float(x):
    """
    Функция проверяет возможность преобразования значения к числу
    :param x: any type
    :return: type bool
    """

    result = bool(0)
    try:
        float(x)
        result = bool(1)
    except ValueError:
        pass
    return result


def my_max(x, y):
    """
    Функция вычисляет наибольшее число из 2х чисел
    :param x: float
    :param y: float
    :return: float
    """
    if x > y:
        result = x
    else:
        result = y
    return result


def my_func(x, y, z):
    """
    Функция суммирует 2 максимальных числа из 3х чисел
    :param x: float
    :param y: float
    :param z: float
    :return: float
    """
    result = my_max(x, y) + my_max(y, z)
    return result


param_list = list()
while True:
    param = input(f"Осталось ввести чисел: {3 - len(param_list)} \n>>>")
    if chek_float(param):
        param_list.append(float(param))
    if len(param_list) == 3:
        break

print(my_func(param_list[0], param_list[1], param_list[2]))
