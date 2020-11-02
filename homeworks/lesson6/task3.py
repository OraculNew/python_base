"""
PEP-8
"""
"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position 
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения 
атрибутов, вызвать методы экземпляров).
"""
# Код программы


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        """Работник
        :param name: Имя
        :param surname: Фамилия
        :param position: Должность
        :param wage: Заработная плата
        :param bonus: Бонус
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        """Функция возвращает полное Имя работника
        """
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        """Возвращает сумму дохода работника
        """
        return super()._income["wage"] + super()._income["bonus"]


new_worker = Position(input("Введите Имя сотрудника\n>>>"),
                      input("Введите Фамилию сотрудника\n>>>"),
                      input("Введите Должность сотрудника\n>>>"),
                      int(input("Введите Оклад сотрудника\n>>>")),
                      int(input("Введите Премию сотрудника\n>>>")),)

print(f"Создан новый сотрудник {new_worker.get_full_name()} на зарплату {new_worker.get_total_income()}")
