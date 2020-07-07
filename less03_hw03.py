'''
    lesson03_hw03
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

'''Функция принимает 3 позиционных аргумента'''

def my_func(a, b, c):
    '''Формируем список для вычислений'''
    tmp = [a, b, c]
    '''Находим минимальное значение аргумента и удаляем из списка'''
    tmp.remove(min(a, b, c))
    '''Возвращаем сумму элементов'''
    return sum(tmp)

'''Ввод данных'''
def init():
    '''Вызов функции обработки данных пользователя'''
    while True:
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            c = int(input('Введите третье число: '))
            return my_func(a, b, c)
        except ValueError:
            print('Вы ввели неверное число')

'''Инициализация программы'''
print(init())
