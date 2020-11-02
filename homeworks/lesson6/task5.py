"""
PEP-8
"""
"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw 
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), 
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен 
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого 
экземпляра.
"""
# Код программы


class Stationery:
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Рисует {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисует {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Рисует {self.title}")


new_stationery = Stationery("Канцелярская принадлежность")
new_pen = Pen("Ручка")
new_pencil = Pencil("Карандаш")
new_handle = Handle("Маркер")

new_stationery.draw()
new_pen.draw()
new_pencil.draw()
new_handle.draw()
