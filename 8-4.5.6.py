class Warehous:

    def __init__(self, city, street, name):
        self.city = city
        self.street = street
        self.name = name
        self.list_of_unit = {
            'Printer' : {},
            'Scanner' : {},
            'Xerox' : {}
            }

    def setunit(self, *unit):
        for i in unit:
            #Я понимаю что тут можно было спокойно реализовать
            #собственное исключени. Но я не увидел в это смысла.
            if not isinstance(i, tuple):
                i = (i, 1)
            elif not isinstance(i[1], int):
                print(f'Кол-во экземпляров долно быть числом!.\n\
Вы ввели "Кол-во {i[0].name} = {i[1]}"')
                continue
            elif not isinstance(i[0], Printer|Scanner|Xerox):
                print(f'Необходимо вносить оргтехнику!\n\
Вы внесли {i[0]}')
                continue
            try:
                # i[0] класс; i[1] кол-во
                self.list_of_unit[type(i[0]).__name__][i[0].name][1] += i[1]
            except KeyError:
                self.list_of_unit[type(i[0]).__name__][i[0].name] = [i[0], i[1]]

    def getunit(self, *unit):
        for i in unit:
            if not isinstance(i, tuple) or len(i) < 3:
                print(f'Формат ввода должен быть "Тип, Модель(наименование), кол-во"\n\
Вы ввели {i}')
            elif not isinstance(i[2], int):
                print(f'Кол-во экземпляров долно быть числом!.\n\
Вы ввели "Кол-во {i[1].name} = {i[2]}"')
                continue
            elif not i[0] in 'Printer|Scanner|Xerox':
                print(f'Необходимо запрашивать оргтехнику!\n\
Вы запросили {i[0]}')
                continue
            try:
                # i[0] Тип оргтехники; i[1] модель, i[2] кол-во
                self.list_of_unit[i[0]][i[1]][1] -= i[2]
                if self.list_of_unit[i[0]][i[1]][1]:
                    print(f'Склад смог выдать лишь \
{i[2] + self.list_of_unit[i[0]][i[1]][1]} ед. {i[1]}.\nОсталось едениц {i[1]}: 0')
                    self.list_of_unit[i[0]][i[1]][1] = 0
                else:
                    print(f'Выдано  \
{i[2] - self.list_of_unit[i[0]][i[1]][1]} ед. {i[1]}.\nОсталось едениц: \
{self.list_of_unit[i[0]][i[1]][1]}')
            except KeyError:
                print('Данное наименование отсутствует на складе')
        
    @property
    def show(self):
        #Какой ужас
        for i in self.list_of_unit.items():
            it = iter(i[1].items())
            print(next(it)[0].rjust(15)
                  + f': {next(iter(i[1].items()))[1][1]}' + f'\r{i[0]}:\n'
                  + ''.join(j[0].rjust(15) + f': {j[1][1]}\n'
                            for j in  it))
        
                    
            

class Unit:

    def __init__(self, name, volume, power, weight, price):
        self.volume = volume
        self.power = power
        self.weight = weight
        self.price = price
        self.name = name

    def name(self):
        return 'Еденица'

class Printer(Unit):

    def __init__(self, name, volume, power, weight, price, color):
        super().__init__(name, volume, power, weight, price)
        self.color = color

class Scanner(Unit):

    def __init__(self, name, volume, power, weight, price, paper):
        super().__init__(name, volume, power, weight, price)
        self.paper = paper

class Xerox(Unit):

    def __init__(self, name, volume, power, weight, price, color, paper):
        super().__init__(name, volume, power, weight, price)
        self.paper = paper
        self.color = color

p_1 = Printer('x213', '0.35 м^2', 50, 3.4, 5000, 'чб')
p_2 = Printer('y213', '0.25 м^2', 150, 5.1, 15000, 'Цветной')
p_3 = Printer('z213', '0.3 м^2', 100, 2.7, 3000, 'чб')
s_1 = Scanner('zHP', '0.1 м^2', 100, 1.8, 7000, 'А4')
x_1 = Xerox('xxx', '0.5 м^2', 250, 10, 27000, 'чб', 'А3')
sf = 345

wh = Warehous('Владивосток', 'пр.Красного знамени', 'Клевер')
wh.setunit(
    (p_1, 4),
    (p_2, 4),
    (sf, 1),
    (p_3),
    (s_1, 3),
    (x_1, 3),
    (x_1, 'n')
    )
print(wh.list_of_unit['Xerox']['xxx'][0].power)
wh.getunit(('Scanner', 'zHP', 4))
wh.show







