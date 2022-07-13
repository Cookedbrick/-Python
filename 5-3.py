with open('5-3.txt') as my_file:
    print('Сотрудники с окладом ниже 20к:\n' +''.join(
         i.split()[0] + '\n' for i in my_file if int(i.split()[1]) < 20000))
    my_file.seek(0)
    print('Средняя ЗП',
         sum(int(i.split()[1]) for i in my_file)/(
             my_file.seek(0) + sum(1 for i in my_file)))