"""
PEP-8
"""
"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, 
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
# Код программы


def fact(n):
    """Генератор факториала числа n
    :param n: число для которого вычисляется факториал
    :return: значение факториала n!
    """
    i = 1
    result = 1
    while n + 1 > i:
        result *= i
        yield result
        i += 1


param = int(input('Введите целое число\n>>>'))

idx = 0
for el in fact(param):
    idx += 1
    print(f"{idx}! = {el}")
