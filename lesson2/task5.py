"""
PEP-8
"""
"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы 
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
# Код программы
var_list = [7, 5, 3, 3, 2]
new_rating = input("Введите новое значение рейтинга в виде натурального числа\n>>>")

max_value = var_list[0]
min_value = var_list[-1]

mistake = bool(0)
try:
    new_rating = int(new_rating)
    if new_rating <= 0:
        mistake = bool(1)
except ValueError:
    mistake = bool(1)

if mistake:
    print("Введите натуральное число!")
else:
    if new_rating > max_value:
        var_list.insert(0, new_rating)
    elif new_rating < min_value:
        var_list.append(new_rating)
    else:
        n = 0
        while 1:
            n = n - 1
            if new_rating >= var_list[-n]:
                var_list.insert(n-1, new_rating)
                break
print(var_list)
