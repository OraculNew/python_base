"""
PEP-8
"""
"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, 
на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и  
выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат: 
1-й день: 2
"""

# Код программы
days = 1
first_km = input("Введите сколько киломметров пробежал спортсмен в первый день\n>>>:")
end_km = input("Введите сколько киломметров необходимо пробежать спортсмену\n>>>:")

print("Результат:")
print(f"1-й день: {first_km}")
if first_km and end_km:
    first_km = float(first_km)
    end_km = float(end_km)
    result = first_km
    while result < end_km:
        days = days + 1
        result = result * 1.1
        print(f"{days}-й день: {result:0.2f}")

print(f"Ответ: на {days}-й день спортсмен достиг результата — не менее {end_km:0.0f} км")
