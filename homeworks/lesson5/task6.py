from functools import reduce
import re
import homeworks.lesson5.my_func as mf
"""
PEP-8
"""
"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести 
словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
# Код программы


def read_numbers(param):
    """
    Возвращает список чисел встречающихся в строке. Вычисляется регулярными выражениями
    :param param: строка в которой производится поиск чисел
    :return: список с числами
    """
    list_values = re.findall(r"[0-9]+", param)
    return list_values


lessons = dict()
with open("file_task6.txt", "r", encoding="UTF-8") as my_file:
    while True:
        content = my_file.readline()
        if not content:
            break
        lessons_key = ''.join(content.split(":")[0])
        values_list = read_numbers(content)
        values = [mf.to_int(value) for value in values_list]
        hours_value = reduce(lambda val, agg: agg + val, values)
        lessons.setdefault(lessons_key, hours_value)
print(lessons)
