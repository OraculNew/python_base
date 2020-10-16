"""
PEP-8
"""
"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

# Код программы
step = 60
seconds = input("Введите время в секундах\n>>>:")

hours = int(seconds) // (step * step)
minutes = (int(seconds) // step) - hours * step
sec = int(seconds) - minutes * step - hours * step * step
print(f"{hours:>02}:{minutes:>02}:{sec:>02}")
