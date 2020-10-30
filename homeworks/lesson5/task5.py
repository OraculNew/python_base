import random
from functools import reduce
import homeworks.lesson5.my_func as mf
"""
PEP-8
"""
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
# Код программы

with open("file_task5.txt", "w", encoding="UTF-8") as my_file:
    inx = 0
    max_value = 1004
    list_float = list()
    while inx < max_value:
        inx += 1
        new_text = str(random.random() // 0.01)
        if not inx % 20:
            new_text = new_text + "\n"
        else:
            new_text = new_text + " "
        list_float.append(new_text)
    my_file.write(''.join(list_float))

with open("file_task5.txt", "r", encoding="UTF-8") as my_file:
    while True:
        content = my_file.readline()
        values = [mf.to_float(value) for value in content.split("\n")[0].split(" ")]
        if not content:
            break
        result = reduce(lambda val, agg: agg + val, values)
print(f"Сумма значений в файле {result}")
