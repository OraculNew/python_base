"""
PEP-8
"""
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для 
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на 
уроках по ООП.
"""
# Код программы


class QuantityError(Exception):
    def __init__(self, mistake):
        self.mistake = mistake


class Equipment:
    article = ""
    name = ""

    def __init__(self, name: str, article: str):
        self.name = name
        self.article = article

    def __str__(self):
        return f"{self.article} {self.name}"


class Printer(Equipment):
    model = ""

    def __init__(self, name: str, article: str, model: str):
        super().__init__(name, article)
        self.model = model

    def __str__(self):
        return f"Принтер {super(Printer, self).__str__()} {self.model}"


class Scan(Equipment):
    size = ""

    def __init__(self, name: str, article: str, size: str):
        super().__init__(name, article)
        self.size = size

    def __str__(self):
        return f"Сканер {super(Scan, self).__str__()} {self.size}"


class Xerox(Equipment):
    office = False

    def __init__(self, name: str, article: str, office: bool):
        super().__init__(name, article)
        self.office = office

    def __str__(self):
        is_office = ""
        if self.office:
            is_office = "для офиса"
        return f"Ксерокс {super(Xerox, self).__str__()} {is_office}"


class Storage:
    equipments = {}
    name = ""

    def __init__(self, name):
        self.name = name

    def credit_order(self, equipment: Equipment, quantity: int):
        if isinstance(equipment, (type(Xerox), type(Printer), type(Scan))):
            raise TypeError("Нет такой номенклатуры в справочнике")
        value = self.equipments.setdefault(type(equipment).__name__)
        if value is None:
            self.equipments.update({type(equipment).__name__: quantity})
        else:
            self.equipments.update({type(equipment).__name__: value + quantity})
        print(f"На склад поступил товар {equipment} {quantity} шт")

    def expense_order(self, equipment: Equipment, quantity: int, unit: str):
        value = self.equipments.setdefault(type(equipment).__name__)
        if value is None:
            raise ValueError("Нет остатков товара")
        if value < quantity:
            raise QuantityError(f"Недостаточно товара на складе {quantity-value} шт")
        self.equipments.update({type(equipment).__name__: value - quantity})
        print(f"Со склада списан товар {equipment} {quantity} шт в подразделение {unit}")


if __name__ == "__main__":
    main_storage = Storage("Основной склад")

    p1 = Printer("p1", "Canon", "MF1290")
    p2 = Printer("p2", "Epson", "2333")
    p3 = Printer("p3", "Samsung", "ASK")
    p4 = Printer("p4", "Kyocera", "Katana")
    main_storage.credit_order(p1, 10)
    main_storage.credit_order(p2, 2)
    main_storage.credit_order(p3, 4)
    main_storage.credit_order(p4, 1)

    s1 = Scan("s1", "Canon", "middle")
    s2 = Scan("s2", "Epson", "big")
    s3 = Scan("s3", "Samsung", "big")
    main_storage.credit_order(s1, 1)
    main_storage.credit_order(s2, 1)
    main_storage.credit_order(s3, 1)

    m1 = Xerox("m1", "Canon", bool(1))
    m2 = Xerox("m2", "Epson", bool(0))
    main_storage.credit_order(m1, 3)
    main_storage.credit_order(m2, 1)

    print(main_storage.equipments)
    main_storage.expense_order(p2, 1, "Бухгалтерия")
    main_storage.expense_order(p3, 1, "Бухгалтерия")
    main_storage.expense_order(s2, 1, "Бухгалтерия")
    main_storage.expense_order(m2, 1, "Бухгалтерия")
    main_storage.expense_order(p1, 4, "Склад")
    print(main_storage.equipments)
