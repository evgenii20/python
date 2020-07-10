'''
    lesson04_hw04
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''

''' Импорт библиотеки '''
from collections import Counter

'''collections.Counter - вид словаря, который позволяет нам считать количество 
неизменяемых объектов (в большинстве случаев, строк).'''

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# counter = Counter(lst)
'''Counter(lst) - формирует словарь используя значения исходного списка в качестве 
ключей и подсчитывает кол-во встречаемости каждого элемента в списке 
Counter({2: 4, 7: 2, 44: 2, 23: 1, 1: 1, 3: 1, 10: 1, 4: 1, 11: 1})'''
#
# unique = list(counter)
'''Формируется список ключей [2, 7, 23, 1, 44, 3, 10, 4, 11]'''
# print(unique)
'''Цикл проходит по списку ключей вытягивая ".items()" значения и сравнивая уникальность с 1 "n == 1"'''
single = [x for x, n in Counter(lst).items() if n == 1]
print(single)
