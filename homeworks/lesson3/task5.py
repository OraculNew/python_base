"""
PEP-8
"""
"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться 
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь 
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, 
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить 
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
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


def chek_list_to_float(x_list):
    """
    Функция преобразует значения списка к типу float
    :param x_list: список
    :return: список
    """
    result = []
    i = 0
    while i < len(x_list):
        if chek_float(x_list[i]):
            result.append(float(x_list[i]))
        else:
            break
        i = i + 1
    return result


def sum_stock(*args):
    """
    Функция вычисляет сумму входящих элементов
    :param args: float
    :return: float
    """
    result = 0
    for item in args:
        result = result + item
    return result


result_sum = 0

while True:
    var_str = input("Введите числа через пробел\n>>>")
    param_list = var_str.split("#")
    var_list = param_list[0].split(" ")
    result_sum = result_sum + sum_stock(*chek_list_to_float(var_list))
    print(result_sum)
    print(param_list.index(param_list[-1]))
    if param_list.index(param_list[-1]) > 0:
        break
