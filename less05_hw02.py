'''
    lesson05_hw02
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

#from itertools import count
# messages = list()

'''Обработка строк из файла'''
with open("my_file.txt", "r", encoding="utf-8") as my_f:

    try:
        line = 0
        '''1-я обработка строк, строка на входе в виде списка'''
        for i in my_f:
            line += 1
            flag = 0
            word = 0
            '''2-я обработка слов по буквам, для определения спец символа'''
            for j in i:
                if j != ' ' and flag == 0:
                    word += 1
                    flag = 1
                elif j == ' ':
                    flag = 0
            '''Вывод количества символов и сл. символа'''
            print(i, len(i), 'симв.', word, 'сл.')
        '''Вывод количества строк'''
        print(line, 'стр.')

    except IOError:
        print("Error!")