'''
    lesson05_hw03
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''

'''Формирование списка сотрудников и среднего дохода'''
with open("text_3.txt", "r", encoding="utf-8") as my_f:
    my_list = []
    content = my_f.read()
    sp = content.split('\n')
    tmp = []
    name = []
    sum = []
    sumall = []
    try:
        suma = 0.0
        suma_all = 0.0
        flag = 0
        flagall = 0
        # my = {line: line for line in sp}
        for line in sp:
            tmp = line.split()
            if tmp[1] < '20000':
                flag += 1
                name.append(tmp[0])
                sum.append(tmp[1])
            if tmp[1] > '20000':
                flagall += 1
                sumall.append(tmp[1])
        for el2 in sumall:
            suma_all += float(el2)
        for el in sum:
            suma += float(el)

        print(name)
        print(f"Средний доход сотрудников c зарплатой < 20000: {round(suma / flag,1)}")
        print(f"Средний доход всех сотрудников: {round((suma + suma_all) / (flag + flagall), 1)}")

    except ValueError:
        print("Error!")
    except IOError:
        print("Error!")