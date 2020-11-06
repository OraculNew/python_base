import time as td
"""
PEP-8
"""
"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, 
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего 
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, 
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение 
и завершать скрипт.
"""
# Код программы


class TrafficLight:
    _color_time = [7, 2, 10]
    __color_name = ["red", "yellow", "green"]
    __current_value = 0

    def __init__(self):
        """Процедура инициализации светофора. Зависима от библиотеки time
        __color_time - список, время работы каждого сигнала светофора в секундах, красного, желтого и зеленого.
        __color_name - названия цветов светофора в жестко фиксированном порядке обхода: красный, желтый, зеленый.
        Метод прерывается при нарушении порядка переключения светофора
        __current_value: текущий сигнал светофора, по умолчанию красный = 0
        switch_to - метод запускает работу светофора, начиная переключать сигнал с красного света сфетофора
        """
        self._color_time = self._color_time
        self.__color_name = self.__color_name
        self.__current_value = self.__current_value

    def switch_to(self):
        if not self.__color_name == ["red", "yellow", "green"]:
            print("Ошибка. Нарушен порядок переключения светофора!!!")
            exit()
        if len(self._color_time) < 3:
            print("Ошибка. Не верное определение времени работы режимов светофора")
            exit()
        inx = self.__current_value
        if inx >= len(self._color_time):
            inx = 0
        value = int(self._color_time[inx])
        while value:
            if value in [1, 3, 5] and inx in [0, 2]:
                print(f"----- {value}")
            else:
                print(f"{self.__color_name[inx]} {value}")
            td.sleep(1)
            value -= 1
        inx += 1
        self.__current_value = inx
        self.switch_to()


if __name__ == "__main__":
    lighting = TrafficLight()
    lighting.switch_to()
