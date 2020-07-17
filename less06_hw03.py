'''
    lesson06_hw03

3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
surname, position (должность), income (доход). Последний атрибут должен быть защищенным
и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе
Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать
экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''

import time
# import colorsys

class Worker:
    # атрибуты класса

    # методы класса

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        # print(f"Светофор: {self._color}")

class Position(Worker):
   def get_total_income(self):
       return sum(self._income.values())

   def get_full_name(self):
       print(f"\033[33mПолное имя\033[0m: \033[32m{self.name} {self.surname}\033[0m\n"
             f"\033[33mДолжность\033[0m: \033[32m{self.position}\033[0m\n"
             f"\033[33mДоход с учётом премии\033[0m: \033[32m{self.get_total_income()}\033[0m")

w = Position("Иван", "Петрович", "Ген. директор", 50000, 15000) # экземпляр класса
# w.name()
w.get_total_income()
w.get_full_name()
