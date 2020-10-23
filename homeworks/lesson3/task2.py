"""
PEP-8
"""
"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""
# Код программы


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


def my_userinfo(name, surname, y_birth, city, email, telephone):
    """
    Функция выводит Имя, фамилию, год рождения, город проживания, email, телефон в строке
    :param name: строка, имя
    :param surname: строка, фамилия
    :param y_birth: год рождения
    :param city: строка, название города
    :param email: строка, электронный адрес
    :param telephone: строка, номер телефона
    :return: форматированная строка
    """
    return f"имя {name},\
    фамилия {surname},\
    год рождения {y_birth},\
    город проживания {city},\
    email {email},\
    телефон {telephone}"


user_info = ["Имя", "фамилию", "год рождения", "город проживания", "email", "телефон"]
user_param = []

i = 0

while i < len(user_info):
    param = input(f"Введите {user_info[i]} ")
    if i == 2 and not chek_int(param):
        continue
    user_param.append(param)
    i = i + 1

print(my_userinfo(user_param[0], user_param[1], user_param[2], user_param[3], user_param[4], user_param[5]))
