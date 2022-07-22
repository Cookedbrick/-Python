from re import findall

class Date:
    cdate = '00-00-0000' 

    def __init__(self, date):
        Date.cdate = date
        self.date = date

    @classmethod
    # Я так и не понял зачем использовать @classmethod для данной задчи
    # если тут можно спокойно обойтись @staticmethod. Но что бы приминение
    # @classmethod совсем уж не был неоправдо, ввёл переменную класа.
    def number(cls, *date):
        if not date:
            return [int(i) for i in findall('\d+', cls.cdate)]
        else:
            return [int(i) for i in findall('\d+', date[0])]

    @staticmethod
    def valid(date):
        if len(findall('[а-яА-ЯёЁ]+', date)) != 0:
            print('Содержание букв не допускается!')
        elif len(Date.number(date)) < 3:
            print ('Не верный формат ввода. \
Данные должны соответствовать формату ДД-ММ-ГГГГ')
        elif Date.number(date)[0] not in range(1,32):
            print('Кол-во дней привышает допустимое')
        elif Date.number(date)[1] not in range(1,13):
            print('Кол-во месяцев привышает допустимое')
        else:
            print('данные введены корректно')
        

d = Date('16-09-1996')
print(d.number('31-22-2007'))
Date.valid('31-22-2007')

