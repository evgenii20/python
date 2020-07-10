'''
    lesson04_hw05
5. Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

''' Импорт библиотеки '''
from functools import reduce

''' при lst = [i for i in len(range(100, 1001)) if i % 2 == 0] выходит 
TypeError: 'int' object is not iterable'''
# Ниже 2 строки рабочей программы сведены в одну в print()
# lst = [i for i in range(100, 1001) if i % 2 == 0]
# print(reduce(lambda x, y: x * y, lst))
''' В функции reduce можно вставить генератор списка в [] скобках
reduce - применяет указанную функцию к некоторому набору объектов и сводит его к единственному
значению
(lambda x, y: x * y, lst) - это функция в одну строку, '''
print(reduce(lambda x, y: x * y, [i for i in range(100, 1001) if i % 2 == 0]))

