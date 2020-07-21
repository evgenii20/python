'''
    lesson07_hw02

2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на практике
работу декоратора @property.'''

'''Ок'''

from abc import ABC, abstractmethod

class BaseClothes(ABC):
    '''Базовый класс clothes - одежда'''

    # методы класса
    '''Используем для всех предков'''
    # def __init__(self, name):
    #     self.name = name
    '''Вызов абстрактного метода'''
    @abstractmethod
    def quanity_cloth(self):
        pass

class Suit(BaseClothes):
    '''Костюм'''
    def __init__(self, name_suit, height_suit):
        # super().__init__(height_suit)
        self.name_suit = name_suit
        self.height_suit = height_suit
        # self.quanity_suit = quanity_suit

    '''Применение декоратора @property'''
    @property
    def quanity_cloth(self):
        '''Количество одежды'''
        quanity_suit = 2 * float(self.height_suit) + 0.3
        return f'Расход ткани на костюм {self.name_suit}: {quanity_suit:.2f}'
        # pass

class Coat(BaseClothes):
    '''Пальто'''
    def __init__(self,  name_coat, size_coat):
        # super().__init__(size_coat)
        self.name_coat = name_coat
        self.size_coat = size_coat
        # self.quanity_coat = quanity_coat

    @property
    def quanity_cloth(self):
        '''Количество одежды'''
        quanity_coat = float(self.size_coat)/6.5 + 0.5
        return (f'Расход ткани на пальто {self.name_coat}: {quanity_coat:.2f}')

'''Вывод'''
coat = Coat("Gucci", 140)
print(coat.quanity_cloth)
suit = Suit("Ягуар Elit", 180)
print(suit.quanity_cloth)
