def div(num, den):
    try:
        print(f'{num/den:.3}')
    except ZeroDivisionError:
        print('Деление на ноль')


div(int(input('Введите числитель\n')), int(input('Введите знамен.\n')))