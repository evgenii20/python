'''
    lesson05_hw01
1. Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.'''

from itertools import count
# messages = list()

'''Ввод строки и запись в файл'''
with open("my_file.txt", "w", encoding="utf-8") as my_f:

    while True:
        try:
            s = input("Введите строку \nПустая строка для выхода: ")
            if s == '':
                break
            content = my_f.write(s + "\n")
        except IOError:
            print("Error!")
