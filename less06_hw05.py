'''
    lesson06_hw05

5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    # атрибуты класса

    # методы класса

    def __init__(self, title, draww):
        self.title = title
        self.draww = draww

    # def title(self):
    def draw(self):
        # print(f"Запуск отрисовки: {self.draw} в классе по умолчанию {self.title}")
        print(f"Запуск отрисовки: {self.draww} класс Stationery")

class Pen(Stationery):
    # Stationery.title = "Pen"
    def draw(self):
        print(f"Запуск отрисовки: {self.draww} класс Pen")
        # print(f"Запуск отрисовки: {self.draww}")

class Pencil(Stationery):
    # Stationery.title = "Pencil"
    def draw(self):
        # print(f"Запуск отрисовки: {self.draww}")
        print(f"Запуск отрисовки: {self.draww} класс Pencil")

class Handle(Stationery):
    # Stationery.title = "Handle"
    def draw(self):
        # print(f"Запуск отрисовки: {self.draww}")
        print(f"Запуск отрисовки: {self.draww} класс Handle")

'''# s = Pen("Канцелярия", "Фломастер")'''
s = Stationery("Канцелярия", "Фломастер")
s.draw()
s1 = Pen("Канцелярия", "Фломастер")
s1.draw()
s2 = Pencil("Канцелярия", "Фломастер")
s2.draw()
s3 = Handle("Канцелярия", "Фломастер")
s3.draw()