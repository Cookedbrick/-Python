with open('5-3.txt') as my_file:
    print('Кол-во слов в файле', sum(len(i.split()) for i in my_file))
    my_file.seek(0)
    print('Кол-во строк', sum(1 for i in my_file))