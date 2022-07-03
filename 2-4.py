string = input('Введите несколько слов, разделённых пробелами\n')
counter = 1
for i in string.split():
    print ('Слово № %s : %10.10s' % (counter, i))
    counter += 1