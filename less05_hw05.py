'''
    lesson05_hw05
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.'''

'''Ввод чисел и подсчёт чисел из файла'''
with open("my_file5.txt", "w", encoding="utf-8") as my_f:
    s = None

    try:
        s = input("Введите строку из чисел \nразделённых пробелами и нажмите Enter: ")
        content = my_f.write(s + "\n")
    except IOError:
        print("Error!")


with open("my_file5.txt", "r", encoding="utf-8") as my_f5:
    line = 0
    '''1-я обработка строк, строка на входе в виде списка'''
    cont = my_f5.read()
    sp = cont.split('\n')
    tmp1 = 0.0
    sum = 0.0
    word = 0
    for i in sp[:]:
        tmp = i.split()
        if i != '':
            line += 1
        # flag = 0
        '''2-я обработка слов по буквам, для определения спец символа'''
        for j in tmp:
            tmp1 += float(j)
            sum = tmp1
            if j != ' ':
            #     # tmp1 += j
                word += 1
    '''Вывод количества символов и суммы'''
    print(f"Сумма {word} чисел = {sum}")
    '''Вывод количества строк'''
    print(line, 'стр.')

