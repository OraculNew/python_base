from sys import argv
from itertools import cycle, count

"""
PEP-8
"""
"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен 
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором 
также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
# Код программы
script_name, first_param, second_param = argv


for value in count(int(first_param)):
    print(value)
    if value > int(second_param):
        break


col = int(first_param)
for value in cycle(list("ABC")):
    print(value)
    col += 1
    if col > int(second_param):
        break
