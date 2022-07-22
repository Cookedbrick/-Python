class MyZeroDivisionError(Exception):

    def __str__(self):
        return 'Ошибка деления на "0"'

try:
    a = int(input('Введите числитель: '))
    b = int(input('Введите знаменатель: '))
    if not b:
        raise MyZeroDivisionError
    print(a/b)
except TypeError:
    print('Должно быть введено число!')
except MyZeroDivisionError as err:
    print(err)
    


    
