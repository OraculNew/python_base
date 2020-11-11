"""
PEP-8
"""
"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните 
вызов методов и также покажите результат.
"""
# Код программы


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = bool(0)

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction=1):
        if direction:
            direction_where = "право"
        else:
            direction_where = "лево"
        print(f"Автомобиль {self.name} повернул на {direction_where}")

    def show_speed(self):
        print(f"Автомобиль {self.name} едет со скоростью {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль {self.name} движется с превышением скорости {self.speed} км/ч")
        else:
            print(f"Автомобиль {self.name} едет со скоростью {self.speed} км/ч")


class SportCar(Car):
    def show_speed(self):
        super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Автомобиль {self.name} движется с превышением скорости {self.speed} км/ч")
        else:
            print(f"Автомобиль {self.name} едет со скоростью {self.speed} км/ч")


class PoliceCar(Car):
    def show_speed(self):
        super().show_speed()


if __name__ == "__main__":
    new_town_car = TownCar(35, "Blue", "Lada", bool(0))
    new_sport_car = SportCar(135, "Red", "Ferrari", bool(0))
    new_work_car = WorkCar(55, "Yellow", "Feat", bool(0))
    new_police_car = PoliceCar(90, "Black/White", "Ford", bool(1))
    garage = {"Городской автомобиль": new_town_car,
              "Спортивный автомобиль": new_sport_car,
              "Рабочий автомобиль": new_work_car,
              "Полицейский автомобиль": new_police_car}
    print(f"Выберите автомобиль из гаража:")
    inx = 0
    garage_list = list()
    for key, value in garage.items():
        inx += 1
        garage_list.append(value)
        print(f"{inx}. {key}")

    nom = int(input("Укажите выбранный номер автомабиля из гаража\n>>>"))
    current_auto = ""
    if (nom > 0) and (nom <= len(garage_list)):
        current_auto = garage_list[nom-1]
        print(f"Вы выбрали автомобиль:\n"
              f"name {current_auto.name}\n"
              f"color {current_auto.color}\n"
              f"speed {current_auto.speed}\n"
              f"is_police {current_auto.is_police}")
    else:
        exit()

    current_auto.go()
    current_auto.show_speed()
    current_auto.turn(1)
    current_auto.turn(0)
    current_auto.stop()
