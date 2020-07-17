'''
    lesson06_hw04

4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля. Для
классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.'''

'''Ок'''

import time
# import colorsys

class Car:
    # атрибуты класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        # методы класса

    def go(self):
        print(f"Машина \033[33m{self.name}\033[0m поехала: \033[32mGo - Go - Go!\033[0m")

    def stop(self):
        time.sleep(2)
        print(f"Машина остановилась: \033[5m\033[31m STOP\033[0m")

    def torn(self):
        time.sleep(2)
        print(f"Машина поворачивает на право: \033[33m torn right\033[0m")


    def show_speed(self):
        time.sleep(2)
        print(f"Текущая скорость автомобиля: {self.speed}км/ч.")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            time.sleep(3)
            print(f"Скорость \033[5m\033[31m{self.speed}\033[0mкм/ч. "
                  f"\033[5m\033[31m Привышение! Понизьте скорость!\033[0m")
        else:
            time.sleep(2)
            print(f"Скорость автомобиля \033[32m{self.speed}\033[0m - в пределах нормы.")

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            time.sleep(3)
            print(f"Скорость \033[5m\033[31m{self.speed}\033[0m км/ч. "
                  f"\033[5m\033[31m Привышение! Понизьте скорость!\033[0m")
        else:
            time.sleep(2)
            print(f"Скорость автомобиля {self.speed} - в пределах нормы.")

class PoliceCar(Car):
    pass


car = TownCar(100, 'Желтый', 'Lada', 0)
car.go()
car.torn()
car.show_speed()
car = WorkCar(55, 'Желтый', 'Lada', 0)
car.show_speed()
car.stop()

