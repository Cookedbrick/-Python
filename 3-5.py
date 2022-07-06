def my_func(sum = 0):
    string = input('Введите ряд чисел, символ "s"\
прерывает скрипт\n')
    string = string.split()
    for i in string:
        if i == 's': return(sum)
        sum += int(i)
    print(sum)
    sum = my_func(sum)
    return(sum)
print(my_func())
