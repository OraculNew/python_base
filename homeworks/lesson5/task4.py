from translate import Translator
"""
PEP-8
"""
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские 
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
# Код программы
translator = Translator(from_lang="en", to_lang="ru")
with open("file_task4.txt", "r", encoding="UTF-8") as my_file:
    with open("file_task4_translate.txt", "w", encoding="UTF-8") as my_file_translate:
        while True:
            content = my_file.readline()
            if not content:
                break
            content_list = content.split(" ")
            content_list[0] = translator.translate(content).split(' ')[0].title()
            my_file_translate.write(" ".join(content_list))
