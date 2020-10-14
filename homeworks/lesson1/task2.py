"""
PEP-8
"""
"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

# Объявление переменных
seconds: int = 0
hours: int = 0
minutes: int = 0
sec: int = 0
step = 60

# Код программы
seconds = input("Введите время в секундах\n>>>:")

hours = int(seconds) // (step * step)
minutes = (int(seconds) // step) - hours * step
sec = int(seconds) - minutes * step - hours * step * step
print(f"{hours:>02}:{minutes:>02}:{sec:>02}")
