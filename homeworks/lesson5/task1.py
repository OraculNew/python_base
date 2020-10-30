import requests
"""
PEP-8
"""
"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""
# Код программы
with open("file_task1.txt", "w", encoding="UTF-8") as my_file:
    while True:
        inp_text = input("Введите текст\n>>>")
        if not inp_text:
            break
        my_file.write(inp_text+"\n")
