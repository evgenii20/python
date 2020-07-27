'''
    lesson08_hw04 - 05 - 06

4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках
реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''
from builtins import list

from collections import defaultdict

class Warehouse:
    '''Warehouse склад оргтехники. В котором хранится вся оргтехника в виде
    многомерного списка
 {'Scaner': {'B8237C48': ['CANON CanoScan', 3000, 1200, 'A4', 'Scaner']},
 'Xerox': {'C365N65': ['Kyocera Mita', 40000, 2000, 'A4', 'Xerox']},
 'Printer': {'A543N47': ['CANON i-SENSYS', 3500, 600, 'A4', 'Printer']}}
    '''
    warehous_office_dict = defaultdict(dict)


class MyCompany(Warehouse):
    '''Класс описывающий подразделение компании
    Подразделение может брать технику со склада. Хранение техники аналогично складу "Warehouse"
    '''
    my_company_dict = defaultdict(dict)

    @property
    def valid_data_user(self):
        '''Функция позволяет переместить технику с основного склада в подразделение компании'''
        print('Доступная оргтехника на складе')
        list_equipment = []
        for num, key in enumerate(self.warehous_office_dict.keys(), 1):
            print(f'{num}) {key}')
            list_equipment.append(key)
        while True:
            # Проверка ввода данных
            try:
                num_group = int(input('Введите номер доступной оргтехники для просмотра - '))
            except ValueError:
                print('Введите число!')
            else:
                if num_group > 0 and num_group <= (len(list_equipment)):
                    num_group -= 1
                    name_group = list_equipment[num_group]
                    break

        print(f'\nВ группе {name_group} содержится следующая техника:')
        list_item_group_equipment = []
        for num_1, key_1 in enumerate(self.warehous_office_dict[name_group].keys(), 1):
            print(f'{num_1}) Серийный номер ({key_1}) устройство '
                  f'{self.warehous_office_dict[name_group][key_1]}')
            list_item_group_equipment.append(key_1)
        while True:
            try:
                num_item_group = int(input('Введите номер устройства для получения - '))
            except ValueError:
                print('Введите число!')
            else:
                if (num_item_group > 0) and (num_item_group <= (len(list_item_group_equipment))):
                    num_item_group -= 1
                    name_item_group = list_item_group_equipment[num_item_group]
                    break
        print(f'\nВыбрано устройство {self.warehous_office_dict[name_group][name_item_group]} '
              f'серийный номер ({name_item_group}).')
        while True:
            user_confirmation = input('\nДля того что бы забрать устройтсво введите "Y", '
                                      'для отказа "N" - ').lower()
            if user_confirmation == 'y':
                self.my_company_dict[name_group][name_item_group] = self.warehous_office_dict[name_group][
                    name_item_group]
                del self.warehous_office_dict[name_group][name_item_group]
                if self.warehous_office_dict[name_group] == {}:
                    del self.warehous_office_dict[name_group]
                break
            elif user_confirmation == 'n':
                break

        # pass

class OfficeEquipment:
    '''OfficeEquipment - Класс оргтехника базовый для классов наследников'''
    count = 0
    def __init__(self, serial_number, model, price, dpi, paper_size, jet_type): # dpi, paper_size, jet_type):
        self.serial_number = serial_number
        self.price = price
        self.model = model
        self.dpi = dpi
        self.paper_size = paper_size
        self.jet_type = jet_type
        
        self.device_info_dict = {self.serial_number: [self.model, self.price, self.dpi, self.paper_size, self.jet_type]}

    def add_warehouse(self):
        """
        Передаёт новый экземпляр техники на склад.
        """
        # pass
        Warehouse.warehous_office_dict[self.jet_type][self.serial_number] = self.device_info_dict[self.serial_number]
        

class Printer(OfficeEquipment):
    '''Printer наследник класса - OfficeEquipment - Класс оргтехника. В классе Printer
    реализовать уникальные параметры для данного типа техники'''
    def __init__(self, serial_number, model, price, dpi, paper_size, jet_type): 
        super().__init__(serial_number, model, price, dpi, paper_size, jet_type) 
        self.device_info_dict = {
            serial_number: [self.model, self.price, self.dpi, self.paper_size,
                                                         self.jet_type]} 

    # pass

class Scaner(OfficeEquipment):
    '''Scaner наследник класса - OfficeEquipment - Класс оргтехника. В классе Scaner
    реализовать уникальные параметры для данного типа техники'''

    def __init__(self, serial_number, model, price, dpi, paper_size, jet_type):  
        super().__init__(serial_number, model, price, dpi, paper_size, jet_type)  
        OfficeEquipment.count += 1
        self.device_info_dict = {
            serial_number: [self.model, self.price, self.dpi, self.paper_size,
                                    self.jet_type]}  

class Xerox(OfficeEquipment):
    '''Xerox наследник класса - OfficeEquipment - Класс оргтехника. В классе Xerox
    реализовать уникальные параметры для данного типа техники'''

    def __init__(self, serial_number, model, price, dpi, paper_size, jet_type):  
        super().__init__(serial_number, model, price, dpi, paper_size, jet_type)  
        self.device_info_dict = {
            serial_number: [self.model, self.price, self.dpi, self.paper_size,
                                    self.jet_type]}  

warehouse = Warehouse()

my_company = MyCompany()

print('Обозначим принтер')
'''model, price, dpi, paper_size, jet_type'''
pinter = Printer('A543N47', 'CANON i-SENSYS', 3500, 600, 'A4', 'Printer')
print(pinter.device_info_dict)
print()

print('Обозначим сканер')
scaner = Scaner('B8237C48', 'CANON CanoScan', 3000, 1200, 'A4', 'Scaner')
print(scaner.device_info_dict)
print()

print('Обозначим ксерокс')
xerox = Xerox('C365N65', 'Kyocera Mita', 40000, 2000, 'A4', 'Xerox')
print(xerox.device_info_dict)
print()

print('Отправим на склад сканер')
scaner.add_warehouse()
print(warehouse.warehous_office_dict)
print()
print('Отправим на склад ксерокс')
xerox.add_warehouse()
print(warehouse.warehous_office_dict)
print()
print('Отправим на склад принтер')
pinter.add_warehouse()
print(warehouse.warehous_office_dict)

print()
print('Техника необходимая подразделению')
my_company.valid_data_user
print()
print('Техника в подразделении')
print(my_company.my_company_dict)
print()
print('Остатки техники на складе')
print(warehouse.warehous_office_dict)

