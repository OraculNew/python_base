from abc import ABC, abstractmethod
"""
PEP-8
"""
"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого 
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: 
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма 
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные 
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
# Код программы


class Clothes(ABC):
    name = ""
    expenditure = 0

    def __init__(self, name=""):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        Clothes.__init__(self, name)
        self.size = size

    def __str__(self):
        return f"{self.name} {self.size}"

    def calc(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        Clothes.__init__(self, name)
        self.height = height

    def __str__(self):
        return f"{self.name} {self.height}"

    def calc(self):
        return 2 * self.height + 0.3

    @property
    def expenditure(self):
        return self.calc()


if __name__ == "__main__":
    clothes1 = Coat("Пальто", 23)
    clothes2 = Suit("Пиджак маленький", 172)
    clothes3 = Suit("Пиджак средний", 185)
    clothes4 = Suit("Пиджак большой", 195)
    print(clothes1.expenditure)
    print(clothes2.expenditure)
    print(clothes3.expenditure)
    print(clothes4.expenditure)
    print(sum([clothes1.expenditure, clothes2.expenditure, clothes3.expenditure, clothes4.expenditure]))
