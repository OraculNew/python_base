"""
PEP-8
"""
"""
* Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь 
с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать 
программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
# Код программы
products_list = []
param_text = 1
features_list = ["название", "цена", "количество", "ед"]
n = 1

while bool(1):
    param_text = input("""Введите параметры товара через пробел(название, цена, количество, единица). 
    Для выхода нажмите enter\n>>>""")
    if not param_text:
        break
    param_list = param_text.split(" ")
    param_dict = dict(zip(features_list, param_list))
    product = (n, param_dict)
    products_list.append(product)
    n = n + 1

new_dict = dict()

for item in products_list:
    param_list = item[1]
    for item_param in param_list:
        current_list = new_dict.setdefault(item_param)
        if current_list is None:
            new_dict[item_param] = list()
        new_dict[item_param].append(param_list.get(item_param))

# Удаляем дубли значений свойств
for item_result in new_dict:
    new_dict[item_result] = set(new_dict[item_result])
print(new_dict)
