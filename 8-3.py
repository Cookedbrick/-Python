from re import findall

class MyExcept(Exception):

    def __str__(self):
        return 'Должны вводиться только числа.\nПродолжайте ввод.'

l = []
while True:
    l.append(input())
    if l[-1] == 'stop':
        l.pop()
        break
    try:
        if findall('[^-.1-9]', l[-1]) or l[-1] == '':
            raise MyExcept
    except MyExcept as err:
        print(err)
        l.pop()

print('конец', l)
