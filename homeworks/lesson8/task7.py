"""
PEP-8
"""
"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов 
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и 
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
# Код программы


class ComplexNumber:

    def __init__(self, value):
        self.complex = value
        self.real = self.complex.real
        self.imaginary = self.complex.imag

    def __str__(self):
        return f"{self.real} + ({self.imaginary})i"

    def __add__(self, other):
        return ComplexNumber((self.real + other.real) + (self.imaginary + other.imaginary))

    def __mul__(self, other):
        return ComplexNumber(((self.real * other.real) - (self.imaginary * other.imaginary)) +
                             ((self.real * other.imaginary) + (self.imaginary * other.real)))


a = 5 + 3j
b = 6

print(a)
print(b)

print(ComplexNumber(a + b))
print(ComplexNumber(a * b))
