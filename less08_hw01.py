'''
    lesson08_hw01

1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''

class Dates:
    '''Класс Дата'''
    # атрибуты класса
    def __init__(self, date):
        self.date = date

    # методы класса
    '''Использование декоратора'''
    @classmethod
    def import_date(cls, date):
        try:
            int_date = []
            for i in date.split('-'):
                int_date.append(int(i))
            return int_date
        except (ValueError, TypeError):
            print('Please enter correct date. Format: dd-mm-yyyy')

    @staticmethod
    def valid(date):
        try:
            '''Заполнение списка для проверки даты '''
            valid_date = [
                [i for i in range(1, 32)],  # Day
                [i for i in range(1, 13)],  # Month
                [i for i in range(1900, 2021)]  # Year
            ]
            '''Заполнение списка d-m-y '''
            valid_date_names = ['Day', 'Month', 'Year']
            for i in range(len(date)):
                if date[i] in valid_date[i]:
                    print(f'{valid_date_names[i]} is valid')
                else:
                    print(f'{valid_date_names[i]} is invalid')

        except (TypeError, ValueError, IndexError):
            print('Please enter correct date. Format: dd-mm-yyyy')

'''Павильный вызов класса Date'''

date = Dates.import_date("22-07-2020") # dd-mm-yyyy

print(date)
Dates.valid(date)

