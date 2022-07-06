def my_func(x, y):
    degree = x
    for i in range(abs(y)-1):
        degree *= x
    return 1/degree
print('{0:.3}'.format(
        my_func(
        float(input('Введите положительное действительное число\n')), 
        int(input('Введите целое отрицательное число\n'))
        )))

