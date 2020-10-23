"""
PEP-8
"""
"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с 
прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово 
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""
# Код программы


def int_func(word):
    """
    Фукнция возвращает слово с первой прописной буквой
    :param word: str
    :return: str
    """
    return f"{word[0].upper()}{word[1:].lower()}"


def my_map(used_func, iter_obj):
    """
    Функция которая позволяет вызвать другую функцию на каждый эелемент итерируемого объекта
    :param used_func: функция
    :param iter_obj: итерируемый объект
    :return:
    """
    for itm in iter_obj:
        yield used_func(itm)


param = input('Введите строку из слов, разделенных пробелом\n>>>')
my_list = param.split()
result = list(my_map(int_func(' '), my_list))
print(*result)
