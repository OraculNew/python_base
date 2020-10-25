import homeworks.lesson4.my_func as mf
"""
PEP-8
"""
"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
# Код программы
print(list(itm for itm in mf.my_range(20, 241) if not itm % 20 or not itm % 21))
