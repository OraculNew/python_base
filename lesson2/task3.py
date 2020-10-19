"""
PEP-8
"""
"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# Код программы
season_1 = [12, 1, 2]
season_2 = [3, 4, 5]
season_3 = [6, 7, 8]
season_4 = [9, 10, 11]
var_disc = {"Зима": season_1, "Весна": season_2, "Лето": season_3, "Осень": season_4}

nom_month = input("Введите номер месяца года\n>>>")

result = "Нет такого номера месяца!"
try:
    nom_month = int(nom_month)
    for item in var_disc:
        if nom_month in var_disc.get(item):
            result = f"Введенный номер месяца относится к времени года: {item}"
    print(result)
except ValueError:
    print("Ошибка преобразования в целое число")
