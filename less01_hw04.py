'''
    lesson01_hw04
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''

number_one = int(input('Введите целое положительное число: '))
num_max = number_one % 10
number_two = number_one // 10
while number_two > 0:
    if num_max == 9:
        break
    if number_two % 10 > num_max:
        num_max = number_two % 10
        number_two = number_two // 10
    else:
        number_two = number_two // 10
print(f'Самая большая цифра в числе "{number_one}":', num_max)
