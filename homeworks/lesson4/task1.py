from sys import argv
"""
PEP-8
"""
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами.
"""
# Код программы
script_name, first_param, second_param, third_param = argv


def calc_salary(all_hours, rate_hours, bonus):
    return all_hours * rate_hours + bonus


print(calc_salary(float(first_param), float(second_param), float(third_param)))
