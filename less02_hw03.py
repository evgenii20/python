'''
    lesson02_hw03
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

# month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
# winter - зима; spring - весна; summer - Лето; autumn - Осень; season - сезон
year_dict = {
    'season': {
        'winter': ['Зима', 12, 1, 2],
        'spring': ['Весна', 3, 4, 5],
        'summer': ['Лето', 6, 7, 8],
        'autumn': ['Осень', 9, 10, 11]
    }
}
res = []
month = 0
while month <= 0:
    month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
for season, months in year_dict['season'].items():
    for el in months:
        if el == month:
            res = months[0]
print(f"Месяц '{month}' относится к времени года: {res}")
