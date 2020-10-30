import json
from functools import reduce
import homeworks.lesson5.my_func as mf
"""
PEP-8
"""
"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма 
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
# Код программы
firms = dict()
profit_list = list()
with open("file_task7.txt", "r", encoding="UTF-8") as my_file:
    while True:
        content = my_file.readline()
        if not content:
            break
        content_list = content.split(" ")
        firm_key = "".join(content_list[1]) + " " + "".join(content_list[0])
        values_list = content_list[2:]
        values = [mf.to_float(value) for value in values_list]
        profit = reduce(lambda val, agg: val - agg, values)
        firms.setdefault(firm_key, profit)
        if profit > 0:
            profit_list.append(profit)

if len(profit_list):
    average_profit = reduce(lambda val, agg: val + agg, profit_list) / len(profit_list)
else:
    average_profit = 0

result_list = list()
result_list.append(firms)
result_list.append({"average_profit": average_profit})

with open('file_task7.json', 'w', encoding='UTF-8') as my_file:
    json.dump(result_list, my_file, ensure_ascii=False, indent=1)
