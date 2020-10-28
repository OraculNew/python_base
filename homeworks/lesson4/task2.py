"""
PEP-8
"""
"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
"""
# Код программы
inx = 0
with open("file_task2.txt", "r", encoding="UTF-8") as my_file:
    while True:
        content = my_file.readline()
        if not content:
            break
        inx += 1
        list_words = content.split(" ")[:-1]
        print(f"В {inx} строке: {len(list_words)} слов(а)")
print(f"Всего строк в файле {inx}")
