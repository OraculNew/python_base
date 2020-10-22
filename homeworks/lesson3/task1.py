"""
PEP-8
"""
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
# Код программы


def chek_float(x):
    """
    Функция проверяет возможность преобразования значения к числу
    :param x:
    :return type bool:
    """

    result = bool(0)
    try:
        float(x)
        result = bool(1)
    except ValueError:
        pass
    return result


def my_division(top, bottom):
    """
    Функция выполняет математическое деление чисел
    :param top: число являющееся числителем
    :param bottom: число являющееся знаменателем
    :return: type float
    """
    if bottom == 0:
        return float("nan")
    return top / bottom


number1 = input("Введите число - числитель\n>>>")
number2 = input("Введите число - знаменатель\n>>>")

if chek_float(number1) and chek_float(number2):
    print(my_division(float(number1), float(number2)))
else:
    print("Введеные значения должны быть числами")
