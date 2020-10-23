"""
PEP-8
"""
"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение 
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо 
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
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


def chek_int(x):
    """
    Функция проверяет возможность преобразования значения к целому числу
    :param x: any type
    :return: type bool
    """

    result = bool(0)
    try:
        int(x)
        result = bool(1)
    except ValueError:
        pass
    return result


def my_func_1(x, y):
    """
    Функция возведения в степень y, значения x. Через способ 1 (**)
    :param x: float
    :param y: int
    :return: float
    """
    result = x ** y
    return result


def my_func_2(x, y):
    """
    Функция возведения в степень y, значения x. Через способ 2 (через цикл)
    :param x: float
    :param y: int
    :return: float
    """
    i = my_abs(y)
    val = i == y
    result = 1
    while i > 0:
        if val:
            result = result * x
        else:
            result = result / x
        i = i - 1

    return result


def my_abs(x):
    """
    Функция возвращает модуль от числа
    :param x: float
    :return: положительное число
    """
    if x < 0:
        x = -x
    return x


control = False

param1 = 0
while not control:
    param1 = input("Введите действительное положительное число\n>>>")
    control = chek_float(param1)
    if chek_float(param1):
        control = my_abs(float(param1)) == float(param1)
        param1 = float(param1)

control = False

param2 = 0
while not control:
    param2 = input("Введите отрицательное целое число\n>>>")
    control = chek_int(param2)
    if control:
        control = param2 == str(int(param2)) and -my_abs(int(param2)) == int(param2)
        param2 = int(param2)


print(f"Первый способ: {my_func_1(param1, param2)}")
print(f"Второй способ: {my_func_2(param1, param2)}")
