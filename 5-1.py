
with open('5-1.txt', 'w') as my_file:
    while True:
        line = input('Введите данные\n')
        if line == '': break
        my_file.write(line + '\n')