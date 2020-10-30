"""
PEP-8
"""
"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, 
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней 
величины дохода сотрудников.
"""
# Код программы
inx = 0
result = 0
with open("file_task3.txt", "r", encoding="UTF-8") as my_file:
    while True:
        content = my_file.readline()
        if not content:
            break
        inx += 1
        data_list = content.split(" ")
        salary = float(data_list[-1])
        if salary < 20000:
            print(*data_list[0:-1])
        result = result + salary
if inx:
    print(f"Средний доход сотрудников {result/inx:.2f} руб.")
