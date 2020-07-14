'''
    lesson05_hw04
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок
строк должен записываться в новый текстовый файл.'''

from collections import Counter

rus_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
tmp = []
'''Перевод числительных при сравнении со списком'''
with open("text_4.txt", "r", encoding="utf-8") as my_f:
    my_list = []
    content = my_f.read().split("\n")
    number = []

    try:
        for line in content:
            line = line.split(' - ')
            number.append(rus_dic[line[0]] + " - " + line[1] + "\n")

    except ValueError:
        print("Error!")
        # content = my_f.write(s + "\n")
    except IOError:
        print("Error!")

'''Запись в файл'''
with open("text_4_1.txt", "w", encoding="utf-8") as my_f4:
    # while True:
    try:
        for i in number:
            my_f4.write(i)
            print(i, end='')
    except IOError:
        print("Error!")
